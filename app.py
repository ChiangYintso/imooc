from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ABCabc123!@#@127.0.0.1/mysql'
db = pymysql.connect(host='localhost',
                    user='root',
                    password='ABCabc123!@#',
                    db='mysql',
                    )

@app.route('/')
def index():
    return "index"


@app.route('/hello')
def hello():
    with db.cursor() as cursor:
        sql = "SELECT * FROM `user`"
        cursor.execute(sql)
        res = cursor.fetchone()
        for row in res:
            app.logger.info(row)
        print("哈哈哈哈")
        return "hello"

if __name__ == '__main__':
    try:
        app.run(debug=True)
    finally:
        db.close()
