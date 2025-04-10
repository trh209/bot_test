from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/respond", methods=["POST"])
def respond():
    data = request.get_json()
    message = data.get("message", "")
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    return jsonify({
        "response": f"당신의 메시지: {message}"
        "time": now
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
