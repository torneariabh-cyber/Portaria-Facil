# ACESS PORT IA — primeira implementação

Esta pasta é um módulo independente para ser adicionado à raiz do repositório Portaria-Facil.
Ela não altera `index.html`, `condominio.html`, `portaria.html` nem os módulos existentes.

## Conteúdo
- `frontend/index.html`: painel inicial responsivo.
- `frontend/styles.css`: identidade visual e responsividade.
- `frontend/app.js`: integração com API e estados reais de conexão.
- `backend/main.py`: API FastAPI inicial.
- `backend/requirements.txt`: dependências Python.
- `.env.example`: exemplo de configuração sem credenciais.
- `.gitignore`: proteção de arquivos locais e segredos.

## Rodar o painel
Abra `frontend/index.html` no navegador. Sem API disponível, o painel informa que o serviço está desconectado e mantém as câmeras como aguardando conexão.

## Rodar a API localmente
```bash
cd backend
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```
Depois, no painel, a API padrão é `http://127.0.0.1:8000`. Para alterar, use o botão "Configurar API".

## Endpoints iniciais
- `GET /api/v1/health`
- `GET /api/v1/cameras`
- `GET /api/v1/events`
- `GET /api/v1/vehicles`

As quatro câmeras são cadastradas como `pending`. Nenhuma câmera é marcada como online sem teste de conexão real.

## Próxima etapa
Validar o computador da portaria, os substreams RTSP do DVR e a conectividade local. Não publicar credenciais RTSP nem abrir a porta 554 diretamente na internet. A integração deve usar VPN/túnel seguro e variáveis de ambiente.
