from fastapi import FastAPI, HTTPException, status
import google.generativeai as genai
import json
import os

from schemas import FeedbackRequest, FeedbackResponse
from prompt_templates import build_analysis_prompt

app = FastAPI(
    title="iFood AI Sentiment & Classification Service",
    description="API para triagem automatizada de chamados de suporte com IA Generativa.",
    version="1.0.0"
)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

@app.get("/", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "online", "service": "iFood AI Feedback Triager"}

@app.post("/analyze-feedback", response_model=FeedbackResponse, status_code=status.HTTP_200_OK)
async def analyze_feedback(data: FeedbackRequest):
    if not data.comment.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="O comentário não pode ser vazio."
        )

    # Modo de simulação local (caso você não tenha colocado uma chave de API no terminal)
    if not GEMINI_API_KEY:
        is_atraso = "atraso" in data.comment.lower() or "demorou" in data.comment.lower()
        return FeedbackResponse(
            order_id=data.order_id,
            sentiment="NEGATIVO" if is_atraso else "NEUTRO",
            category="ATRASO" if is_atraso else "OUTROS",
            urgency_score=4 if is_atraso else 2,
            suggested_reply="[Simulação Local] Pedimos desculpas pelo ocorrido! Nosso time está verificando seu pedido."
        )

    try:
        # Chamada usando a SDK oficial estável
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = build_analysis_prompt(data.comment)

        response = model.generate_content(prompt)
        raw_text = response.text.strip()
        
        if raw_text.startswith("```json"):
            raw_text = raw_text.replace("```json", "").replace("```", "").strip()

        ai_data = json.loads(raw_text)

        return FeedbackResponse(
            order_id=data.order_id,
            sentiment=ai_data.get("sentiment", "NEUTRO"),
            category=ai_data.get("category", "OUTROS"),
            urgency_score=ai_data.get("urgency_score", 3),
            suggested_reply=ai_data.get("suggested_reply", "Obrigado pelo feedback!")
        )

    except json.JSONDecodeError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro ao processar o formato da resposta retornado pela IA."
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Serviço de IA indisponível: {str(e)}"
        )