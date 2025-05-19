from flask import Flask

class Config:
    SECRET_KEY = 'sua_chave_secreta_aqui'
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///salgados_festa.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config.from_object(Config)