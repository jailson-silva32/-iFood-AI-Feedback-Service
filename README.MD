# 🚀 iFood AI Feedback Service

Microserviço assíncrono desenvolvido em **Python** e **FastAPI** para triagem inteligente e análise automatizada de comentários de clientes, utilizando modelos de IA Generativa.

---

## 🎯 O Problema de Negócio

Em horários de pico, o time de atendimento do suporte manual pode enfrentar um alto volume de chamados. A triagem manual de cada comentário para identificar o problema (atraso, troca de prato, falta de itens) pode levar vários minutos por atendimento.

## 💡 A Solução

Esta API recebe os feedbacks dos clientes em tempo real e utiliza a API do Gemini com engenharia de prompts avançada para:
1. **Classificar o Sentimento** (`POSITIVO`, `NEUTRO`, `NEGATIVO`).
2. **Categorizar a Ocorrência** (`ATRASO`, `COMIDA_INCORRETA`, `ITEM_FALTANTE`, etc.).
3. **Atribuir uma Nota de Urgência** (de 1 a 5 para priorizar a fila de chamados).
4. **Gerar uma Resposta Sugerida** em formato JSON pronto para o atendente utilizar no chat.

Tudo isso é processado em **poucos milissegundos**, reduzindo drasticamente o tempo de triagem manual.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.10+
- **Web Framework:** FastAPI (rotas assíncronas de alta performance)
- **Servidor Web:** Uvicorn
- **Validação de Dados:** Pydantic (tipagem estrita)
- **IA Generativa:** Google Gemini API (`gemini-1.5-flash`)

---

## ⚙️ Como Executar o Projeto Localmente

### 1. Clonar o repositório
```bash
git clone [https://github.com/SEU-USUARIO/ifood-ai-feedback-service.git](https://github.com/SEU-USUARIO/ifood-ai-feedback-service.git)
cd ifood-ai-feedback-service