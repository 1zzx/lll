from flask import Flask,render_template
import sqlite3

app = Flask(__name__)


@app.route('/index')
def index():  # put application's code here
    infos = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select * from movie250 limit 0,10"
    data = cur.execute(sql)
    for item in data:
        infos.append(item)

    score = []
    num = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select score,count(score) from movie250 group by score"
    data1 = cur.execute(sql)
    for item in data1:
        score.append(item[0])
        num.append(item[1])
    datalist = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select score,sum(rated) from movie250 group by score"
    data2 = cur.execute(sql)
    for item in data2:
        datalist.append([item[0],item[1]])
    cur.close()
    con.close()
    return render_template('index.html',infos=infos,score=score,num=num,datalist=datalist)


if __name__ == '__main__':
    app.run()
