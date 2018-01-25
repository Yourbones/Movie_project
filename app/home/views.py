#coding:utf-8
from . import home


@home.route("/")
def index():
    return "<h1 style='color:green'>This is home!</h1>"

