from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        custom_data = {}
        # Exemple d'ajout d'un code personnalisé en fonction des erreurs
        for field, errors in response.data.items():
            custom_data[field] = {
                "code": f"ERR_{field.upper()}",
                "message": errors[0] if errors else "Erreur"
            }
        response.data = custom_data
    return response
