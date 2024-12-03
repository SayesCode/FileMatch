from fastapi import APIRouter, UploadFile, File, HTTPException
from src.utils.mime_utils import validate_mime
from src.hooks.mime_hooks import pre_validation, post_validation

router = APIRouter()

@router.post("/validate-file/")
async def validate_file(file: UploadFile = File(...)):
    """
    Valida se o MIME do arquivo corresponde à extensão.
    """
    file_path = file.filename

    # Pré-validação
    pre_validation(file_path)

    # Lê o conteúdo do arquivo diretamente sem salvar no disco
    content = await file.read()

    # Validação
    is_valid = validate_mime(file_path, content)

    # Pós-validação
    post_validation(file_path, is_valid)

    if not is_valid:
        mime_type = get_mime_type(content)
        raise HTTPException(
            detail=f"MIME do arquivo não corresponde à extensão. MIME detectado: {mime_type}."
        )

    return {"status": "success", "message": f"O arquivo '{file_path}' é válido."}

