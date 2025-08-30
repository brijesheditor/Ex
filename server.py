from flask import Flask
import threading
from Extractor import __main__  # मान लेते हैं कि bot यहाँ से start होता है

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running fine ✅"

def run_bot():
    __main__.main()   # जहाँ से bot start होता है, वही function call करो

if __name__ == "__main__":
    # bot को अलग thread में चलाओ
    threading.Thread(target=run_bot).start()
    # साथ में HTTP server भी चलेगा
    app.run(host="0.0.0.0", port=10000)
