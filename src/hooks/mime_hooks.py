def pre_validation(file_path: str):
    """
    Hook executado antes da validação.
    """
    print(f"[HOOK] Pré-validação iniciada para: {file_path}")

def post_validation(file_path: str, is_valid: bool):
    """
    Hook executado após a validação.
    """
    status = "válido" if is_valid else "inválido"
    print(f"[HOOK] Pós-validação: {file_path} é {status}")
