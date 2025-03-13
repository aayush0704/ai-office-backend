from flask import Flask, request, jsonify
from flask_cors import CORS
from nlp_agent import generate_ai_response
from leave_agent import process_leave_request
from certificate_agent import generate_certificate
from query_agent import fetch_academic_info

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    user_id = request.json.get('user_id', 1)

    if "leave" in user_input.lower():
        response = process_leave_request(user_id)
    elif "certificate" in user_input.lower():
        certificate_type = "bonafide" if "bonafide" in user_input.lower() else "noc"
        response = generate_certificate(user_id, certificate_type)
    elif any(word in user_input.lower() for word in ["exam", "calendar", "schedule"]):
        response = fetch_academic_info(user_id, user_input)
    else:
        response = generate_ai_response(user_input)

    return jsonify({"reply": response})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if PORT is not set
    app.run(debug=True, host='0.0.0.0', port=port)
