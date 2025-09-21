from flask import Flask, request, render_template
from getMatchData import getMatchData

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        gameName = request.form['gameName']
        tagLine = request.form['tagLine']
        # getMatchData가 tier도 반환한다고 가정
        result, wins, summoner_name, tier = getMatchData(gameName, tagLine)
        return render_template('search.html', result=result, wins=wins, summoner_name=summoner_name, tier=tier)

    return render_template('search.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form['keyword']
        print("유저의 입력은:", user_input, "입니다.")

        output = [70, 80, 90, 100, 101]
        dic = {
            "name": "이주원",
            "age": 16,
            "hobby": ["축구", "롤"]
        }
        return render_template('index.html', result=output, dic=dic)

    return render_template('index.html')  # 공백 제거

if __name__ == '__main__':
    app.run(port=8000, host="0.0.0.0")
