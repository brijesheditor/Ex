import os
from flask import Flask  # Or whichever framework you use

app = Flask(__name__)

# Define your routes...

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
