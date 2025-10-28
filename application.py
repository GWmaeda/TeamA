# application.py
from flask import Flask, render_template, request
import random

# Flaskのインスタンス。WSGIアプリケーションオブジェクトは'application'
application = Flask(__name__) 

# 抽選の結果のリスト（例）
PRIZES = ["アタリ！", "ハズレ", "もう一度", "参加賞"]

@application.route('/', methods=['GET', 'POST'])
def index():
    # POSTリクエストの場合（ボタンが押された場合）
    if request.method == 'POST':
        # PRIZESリストからランダムに1つを選択
        result = random.choice(PRIZES)
        
        # 結果をHTMLテンプレートに渡して表示
        return render_template('index.html', result=result)
        
    # GETリクエストの場合（初期表示）
    else:
        # 初期表示。resultにはNoneを渡す
        return render_template('index.html', result=None)

if __name__ == "__main__":
    # Elastic Beanstalkではこのブロックは無視されますが、ローカルテスト用として残します。
    application.run(debug=True)