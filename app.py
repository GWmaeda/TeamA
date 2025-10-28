from flask import Flask

application = Flask(__name__)  # EBはapplicationを探す

@application.route('/')
def hello():
    return """
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <title>Hello World</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
    </body>
    </html>
    """

# ローカル実行時のみ app.run を有効に
if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8080, debug=True)
