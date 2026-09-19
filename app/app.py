from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return "Hello, DevOps!", 200


@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON payload provided"}), 400
    return jsonify(data), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)