from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from Chatbot import getResponse

app = Flask(__name__)
CORS(app)

@app.route('prediction", methods=["POST", "OPTIONS')
def prediction():
    if request.method == 'OPTIONS':
        response = jsonify({"message": "CORS Preflight Request Handled"})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        return response

    text = request.get_json().get("message")
    if not text:
        return jsonify({"error": "Message is blank"}), 400

    resource = getResponse(text)
    message = {"answer": resource}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)



