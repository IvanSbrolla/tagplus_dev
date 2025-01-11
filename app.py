from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return 'API Flask no Railway!'

@app.route('/oauth2')
def callback():
    url = 'https://api.tagplus.com.br/oauth2/token'
    code = request.args.get('code', 'None')
    try:
        import requests
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        payload = {
            'grant_type': 'authorization_code',
            'code': code,
            'client_id': 'Xz3uHcC7gc0sQs0N0PdRUFXmpFXx6XmE',
            'client_secret': 'J3JQNgjTzArqfcSvSzzw6vVtqYZo9Cj3'
        }

        response = requests.post(url, data=payload, headers=headers)
        return f'response -> {response}\nresponse content -> {response.content}'

    except Exception as err:
        print(err)
        return code


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)