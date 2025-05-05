
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# Replace with your OpenAI API key
openai.api_key = 'your-api-key-here'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json["message"]

    # Use OpenAI for smart response
    client = OpenAI()

    response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "당신은 대한민국의 분리배출 규정에 따라 정보를 제공하는 챗봇입니다."},
        {"role": "user", "content": user_message}
        ]
    )
    reply = response.choices[0].message.content
    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
