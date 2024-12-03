from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from src.routes.api import router as api_router
import os

app = FastAPI(title="FileMatch API", description="API para validação de MIME e extensão de arquivos.")

app.include_router(api_router, prefix="/api/v1/verify", tags=["File Validation"])

templates_path = os.path.join(os.path.dirname(__file__), "templates")
app.mount("/", StaticFiles(directory=templates_path, html=True), name="static")

@app.middleware("http")
async def redirect_to_root(request: Request, call_next):
    """
    Middleware para redirecionar requisições inválidas para `/`.
    """
    response = await call_next(request)
    if response.status_code == 404 and not request.url.path.startswith("/api/"):
        return RedirectResponse("/")
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
