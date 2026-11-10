from pydantic import BaseModel, Field
from typing import Literal

# Dados que a API RECEBE
class FeedbackRequest(BaseModel):
    order_id: str = Field(..., description="ID único do pedido no iFood")
    comment: str = Field(..., description="Comentário do cliente")

# Dados que a API DEVOLVE
class FeedbackResponse(BaseModel):
    order_id: str
    sentiment: Literal["POSITIVO", "NEUTRO", "NEGATIVO"]
    category: str
    urgency_score: int
    suggested_reply: str