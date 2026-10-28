from flask import Flask

app = Flask(__name__)

VERSION = "1.0.1"

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(port=5000)
