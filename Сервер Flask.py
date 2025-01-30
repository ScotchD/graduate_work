from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/suspicious_cookies', methods=['POST'])
def suspicious_cookies():
    data = request.json
    print("Suspicious cookies received:")
    for cookie in data:
        print(cookie)
    return '', 204

if __name__ == '__main__':
    app.run(port=5000)
