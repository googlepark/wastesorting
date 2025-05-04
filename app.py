
from flask import Flask, render_template, request, jsonify
import openai

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
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who gives waste separation advice in Korea."},
            {"role": "user", "content": user_message}
        ]
    )
    reply = response.choices[0].message["content"]
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
