import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from nlp_agent import generate_ai_response  # Now uses DeepSeek via OpenRouter
from leave_agent import process_leave_request
from certificate_agent import generate_certificate
from query_agent import fetch_academic_info

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    """Handles chat requests from the frontend."""
    user_input = request.json.get('message', "")
    user_id = request.json.get('user_id', 1)

    # Ensure user_input is always a string
    user_input = str(user_input).lower()

    if not user_input.strip():
        return jsonify({"reply": "Error: No message received."}), 400

    try:
        if "leave" in user_input:
            response = process_leave_request(user_id)
        elif "certificate" in user_input:
            certificate_type = "bonafide" if "bonafide" in user_input else "noc"
            response = generate_certificate(user_id, certificate_type)
        elif any(word in user_input for word in ["exam", "calendar", "schedule"]):
            response = fetch_academic_info(user_id, user_input)
        else:
            response = generate_ai_response(user_input)  # Uses DeepSeek API via OpenRouter

        # Check if DeepSeek API returned an error
        if response.startswith("Error:"):
            return jsonify({"reply": response}), 500  # Internal Server Error

    except Exception as e:
        return jsonify({"reply": f"Error processing request: {str(e)}"}), 500

    return jsonify({"reply": response})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use Render's assigned PORT
    print(f"Starting server on port {port}...")  # Debugging log
    app.run(host='0.0.0.0', port=port)  # Ensure binding to 0.0.0.0
