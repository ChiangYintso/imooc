from flask import Flask
from flask_script import Manager
import pymysql
import os


class Application(Flask):
    def __init__(self, import_name):
        super(Application, self).__init__(import_name)
        self.config.from_pyfile('config/base_setting.py')
        self.config.from_pyfile('.flaskenv')
        self.config.from_pyfile('config/{}_setting.py'.format(self.config['FLASK_ENV']))
        self.db = pymysql.connect(host=self.config['DATABASE_HOST'],
                                  user=self.config['DATABASE_USER'],
                                  password=self.config['DATABASE_PASSWORD'],
                                  db=self.config['DATABASE'])


app = Application(__name__)
manager = Manager(app)
