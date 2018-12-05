from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()


def init_ext(app):
    init_db(app)


def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/flaskorm?charset=utf8'
    #
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # 打印sql语句
    app.config['SQLALCHEMY ECHO'] = True
    # app.config['SQLALCHEMY_TRACK']
    db.init_app(app)
    migrate.init_app(app,db)
