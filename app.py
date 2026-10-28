from flask import Flask

app = Flask(__name__)

VERSION = "1.0.0"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return VERSION

if __name__ == "__main__":
    app.run(port=5000)
