from flask import Blueprint

home_bp = Blueprint('home', __name__)

@home_bp.route('/hello/')
def hello():
    return "Hello from Home Page"

@home_bp.route('/test1/')
def test1():
    import time

    print("Printed immediately.")
    time.sleep(4.4)
    return "Hello from test1"

@home_bp.route('/test2/')
def test2():
    import time

    print("Printed immediately.")
    time.sleep(0.4)
    return "Hello from test2"

@home_bp.route('/test3/')
def test3():
    return "Hello from test3"

@home_bp.route('/test4/')
def test4():
    return "Hello for test4"

