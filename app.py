from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from Chatbot import getResponse

app = Flask(__name__)
CORS(app)

# Method to see if server is available
@app.route('/status')
def serverstatus():
    return 'Server is running'

@app.route('/prediction', methods=["POST", "OPTIONS"])
def prediction():
    if request.method == 'OPTIONS':
        response = jsonify({"message": "CORS Preflight Request Handled"})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        return response

    # response validation
    data = request.get_json()
    #if message is blank
    if not data or 'message' not in data or not data['message'].strip():
        return jsonify({"error": "Message is blank"}), 400

    if len(data['message']) > 200:
        return jsonify({"error": "Message is too long"}), 406

    text = request.get_json().get("message")
    if not text:
        return jsonify({"error": "Message is blank"}), 400

    resource = getResponse(text)
    message = {"answer": resource}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)
