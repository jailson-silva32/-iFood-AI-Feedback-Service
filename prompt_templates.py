def build_analysis_prompt(comment: str) -> str:
    return f"""
Você é um assistente de triagem automatizada do suporte do iFood.
Sua tarefa é analisar o comentário do cliente e responder EXCLUSIVAMENTE em formato JSON.

Siga estas regras de classificação:
1. 'sentiment': Classifique em 'POSITIVO', 'NEUTRO' ou 'NEGATIVO'.
2. 'category': Escolha uma das categorias -> 'ATRASO', 'COMIDA_INCORRETA', 'ITEM_FALTANTE', 'ATENDIMENTO' ou 'OUTROS'.
3. 'urgency_score': Número inteiro de 1 (muito baixa) a 5 (urgente/crítico).
4. 'suggested_reply': Escreva uma resposta curta, empática e profissional em português para o atendente usar.

Comentário do cliente: "{comment}"

Formato exato de saída esperado (JSON apenas, sem marcadores de código markdown):
{{
  "sentiment": "NEGATIVO",
  "category": "ATRASO",
  "urgency_score": 4,
  "suggested_reply": "Pedimos desculpas pela demora! Já estamos verificando com o entregador."
}}
"""