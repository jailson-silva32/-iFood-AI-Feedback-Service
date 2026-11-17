from pydantic import BaseModel, Field
from typing import Literal

# Definimos um tipo fechado com as únicas categorias permitidas no sistema
CategoryType = Literal[
    "ATRASO_ROTA",
    "PROBLEMA_ENDERECO",
    "EMBALAGEM_DANIFICADA",
    "COMIDA_INCORRETA",
    "ITEM_FALTANTE",
    "OUTROS"
]

# Dados que a API RECEBE
class FeedbackRequest(BaseModel):
    order_id: str = Field(..., min_length=3, description="ID único do pedido no iFood")
    comment: str = Field(..., min_length=2, description="Comentário ou reclamação do cliente")

# Dados que a API DEVOLVE (blindados contra valores fora de faixa)
class FeedbackResponse(BaseModel):
    order_id: str
    sentiment: Literal["POSITIVO", "NEUTRO", "NEGATIVO"]
    category: CategoryType
    urgency_score: int = Field(
        ..., 
        ge=1,  # greater than or equal (maior ou igual a 1)
        le=5,  # less than or equal (menor ou igual a 5)
        description="Nota de urgência operacional de 1 a 5"
    )
    requires_driver_action: bool = Field(
        ..., 
        description="Indica se o chamado exige contato imediato na rota do entregador"
    )
    suggested_reply: str