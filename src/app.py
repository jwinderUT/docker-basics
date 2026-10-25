import os
from flask import Flask

app = Flask(__name__)
app_env = os.getenv("APP_ENV", "development")

print("🚀 Welcome to the Python Mini App!")
print(f"🌍 Running environment: {app_env}")
print("💡 Fun fact: Python can power websites with just a few lines of code!")


@app.route("/")
def home():
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Python Mini App</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                text-align: center;
                padding: 80px 20px;
            }}
            .card {{
                background: white;
                color: #333;
                padding: 35px;
                border-radius: 16px;
                max-width: 450px;
                margin: auto;
                box-shadow: 0 10px 30px #0003;
            }}
            h1 {{ color: #667eea; }}
            .environment {{
                display: inline-block;
                background: #e8eaff;
                color: #4b55bd;
                padding: 8px 14px;
                border-radius: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 Hello, Python!</h1>
            <p>Your Flask app is running successfully.</p>
            <p>Current environment:</p>
            <span class="environment">{app_env}</span>
            <p>💡 Keep building something useful!</p>
        </div>
    </body>
    </html>
    """


@app.route("/api/status")
def status():
    return {
        "app": "Python Mini App",
        "environment": app_env,
        "status": "running"
    }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", "5000")),
        debug=(app_env == "development")
    )
