def process_leave_request(user_input):
    """Handles leave requests intelligently"""
    if "casual leave" in user_input:
        return "You have 10 casual leaves remaining. Your request is approved."
    elif "sick leave" in user_input:
        return "You have 5 sick leaves left. Please upload medical proof."
    else:
        return "Specify leave type (Casual/Sick/Vacation)."
