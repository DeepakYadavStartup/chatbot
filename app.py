import os
from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

# Get the API key securely
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Load the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/", methods=["GET", "POST"])
def index():
    prompt = ""
    reply = ""
    if request.method == "POST":
        prompt = request.form.get("prompt")
        if prompt:
            response = model.generate_content(prompt)
            reply = response.text
    return render_template("index.html", prompt=prompt, reply=reply)

if __name__ == "__main__":
    app.run(debug=True)




