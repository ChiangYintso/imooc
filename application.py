import os

import pymysql
from flask import Flask
from flask_script import Manager

from common.libs.urlManager import UrlManager


class Application(Flask):
    def __init__(self, import_name, template_folder = None):
        super(Application, self).__init__(import_name, template_folder=template_folder)
        self.config.from_pyfile('config/base_setting.py')
        self.config.from_pyfile('.flaskenv')
        self.config.from_pyfile('config/{}_setting.py'.format(self.config['FLASK_ENV']))
        self.db = pymysql.connect(host=self.config['DATABASE_HOST'],
                                  user=self.config['DATABASE_USER'],
                                  password=self.config['DATABASE_PASSWORD'],
                                  db=self.config['DATABASE'])


app = Application(__name__, template_folder=os.getcwd()+'/web/templates/')
manager = Manager(app)

# template global function
app.add_template_global(UrlManager.buildUrl, 'buildUrl')
app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
