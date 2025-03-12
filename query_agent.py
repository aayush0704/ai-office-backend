def fetch_academic_info(user_input):
    """Handles academic-related queries"""
    if "backlog exam" in user_input:
        return "Next backlog exam is on 25th March."
    elif "academic calendar" in user_input:
        return "You can find the academic calendar on the university website."
    else:
        return "I can help with academic queries. Please specify."
