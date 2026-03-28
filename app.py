
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

services = {
    "premium_insight": "To jest Twoja płatna analiza danych, za którą użytkownik zapłacił 1$."
}

@app.route('/')
def home():
    return "System zarobkowy: Online. Gotowy do obsługi transakcji."

@app.route('/get_content', methods=['GET'])
def get_content():
    api_key = request.args.get('api_key')
    if api_key == "PRO-123":
        return jsonify({"status": "success", "data": services["premium_insight"]})
    else:
        return jsonify({"status": "error", "message": "Brak opłaconego dostępu"}), 403

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
