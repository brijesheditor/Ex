from flask import Flask
import os
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    # Bot ko background me start karo
    try:
        # Ye command Extractor/__main__.py run karega
        subprocess.Popen(["python", "-m", "Extractor"])
    except Exception as e:
        print("Bot already running or failed:", e)

    return "Bot is running ✅"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render automatically PORT assign karega
    app.run(host="0.0.0.0", port=port)
