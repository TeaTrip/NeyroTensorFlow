from flask import Flask, request
from flask import jsonify
from flask import render_template
import json
import random
import needdata
import reg4

app = Flask(__name__)


@app.route('/main')
def main():
    return render_template("main.html")


@app.route('/predictions')
def predictions():
    return render_template('predictions.html')


@app.route('/table')
def table():
    return render_template('table.html')


@app.route('/api/get_student', methods=['POST'])
def get_student_by_id():
    data = request.json
    # Данные для отправки в программуx
    student_id = data['student_id']
    season_id = data['season_id']
    # Вызов функции
    needdata.create_csv(season_id,student_id)

    #
    #
    print(student_id, season_id)
    return jsonify(reg4.predict())


if __name__ == '__main__':
    app.run(debug=True)
