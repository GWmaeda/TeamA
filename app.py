from flask import Flask

application = Flask(__name__)  # EBは 'application' を探す

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
