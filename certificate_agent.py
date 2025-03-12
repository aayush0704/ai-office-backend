def generate_certificate(user_input):
    """Handles certificate generation requests"""
    if "bonafide" in user_input:
        return "Your bonafide certificate request is being processed."
    elif "NOC" in user_input:
        return "Your NOC certificate is being generated."
    else:
        return "Specify certificate type (Bonafide/NOC)."
