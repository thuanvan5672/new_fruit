from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Chatbot API đang chạy trên Render!"})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("question", "")
    answer = f"Chatbot nhận được câu hỏi: {question}"
    return jsonify({"question": question, "answer": answer})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
