from fastapi import APIRouter, UploadFile, File, HTTPException
from src.utils.mime_utils import validate_mime, get_mime_type
from src.hooks.mime_hooks import pre_validation, post_validation

router = APIRouter()

@router.post("/validate-file/")
async def validate_file(file: UploadFile = File(...)):
    """
    Valida se o MIME do arquivo corresponde à extensão.
    """
    file_path = file.filename

    try:
        # Pré-validação
        pre_validation(file_path)

        # Lê o conteúdo do arquivo diretamente sem salvar no disco
        content = await file.read()
        if not content:
            raise HTTPException(status_code=400, detail="O arquivo enviado está vazio.")

        # Validação
        is_valid = validate_mime(file_path, content)

        # Pós-validação
        post_validation(file_path, is_valid)

        if not is_valid:
            mime_type = get_mime_type(content)
            raise HTTPException(
                status_code=400,
                detail=f"MIME do arquivo não corresponde à extensão. MIME detectado: {mime_type}."
            )

        return {"status": "success", "message": f"O arquivo '{file_path}' é válido."}

    except HTTPException as http_exc:
        # Relevanta erros conhecidos com detalhes claros
        raise http_exc
    except Exception as e:
        # Captura erros inesperados e previne erro 500
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")
