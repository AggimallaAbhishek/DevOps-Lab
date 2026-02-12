from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    build_id = os.getenv("BUILD_ID", "Not Available")
    return f"""
    <h1>Hello from Flask 🚀</h1>
    <p><strong>Jenkins Build ID:</strong> {build_id}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
