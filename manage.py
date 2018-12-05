from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager,Server

from apps import create_app

app = create_app()
manager = Manager(app=app)
migrate = Migrate

manager.add_command('start', Server(host='192.168.50.17', port=9000))
# 添加数据库迁移的脚本命令
manager.add_command('db', MigrateCommand)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
