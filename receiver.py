import requests
from flask import Flask, request, jsonify

ALLOWED_IPS = ["127.0.0.1", "0.0.0.0"]
BotId = "TelegramBotId"

# IP whitelist middleware
class IPWhitelistMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        remote_ip = environ.get('HTTP_X_REAL_IP', environ.get('REMOTE_ADDR'))
        if remote_ip not in ALLOWED_IPS:
            # IP not allowed, return Forbidden status
            start_response('403 Forbidden', [])
            return [b'Forbidden: You do not have permission to access this resource.']
        return self.app(environ, start_response)

# Apply IP whitelist middleware
app = Flask(__name__)
app.wsgi_app = IPWhitelistMiddleware(app.wsgi_app)

@app.route('/receive_data', methods=['POST'])
def receive_data():
    """
    Receives data (text and chat_id) in JSON format, sends it to Telegram API,
    and returns a success or error message.
    """
    data = request.json
    if data:
        value1 = data.get('text')
        value2 = data.get('chat_id')
        print(f"Received value1: {value1}")
        print(f"Received value2: {value2}")
        url = f"https://api.telegram.org/bot{BotId}/sendMessage?chat_id={value2}&text={value1}"
        print(url)

        # Send message to Telegram API and handle potential errors
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Telegram API response: {response.json()}")
            return jsonify({"message": "Data received and sent successfully."}), 200
        else:
            print(f"Error sending message to Telegram: {response.status_code}")
            return jsonify({"error": f"Error sending message to Telegram. Status code: {response.status_code}"}), 500
    else:
        return jsonify({"error": "No data received."}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
