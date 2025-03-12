import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from nlp_agent import generate_ai_response
from database import get_leave_balance, store_user_request

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing (CORS) for frontend connection

@app.route('/chat', methods=['POST'])
def chat():
    """Handles chat requests from the frontend."""
    user_input = request.json.get('message')
    user_id = request.json.get('user_id', 1)  # Default to user ID 1 for testing

    if not user_input:
        return jsonify({"reply": "Please enter a message."})

    # Check if the user is asking about leave balance
    if "leave balance" in user_input.lower():
        leave_balance = get_leave_balance(user_id)
        response = f"Your leave balance is {leave_balance} days."
        store_user_request(user_id, "leave_balance_check", "success")

    # Use AI-powered response for other queries
    else:
        response = generate_ai_response(user_input)
        store_user_request(user_id, "chat_query", "success")

    return jsonify({"reply": response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
