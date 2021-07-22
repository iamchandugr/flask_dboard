from flask import Blueprint

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/hello/')
def hello():
    import time

    print("Printed immediately.")
    time.sleep(2.4)
    return "Hello from Contact Page"

@contact_bp.route('/test1/')
def test1():
    import time

    print("Printed immediately.")
    time.sleep(3.4)
    return "Hello from test1"

@contact_bp.route('/test2/')
def test2():
    return "Hello from test2"

@contact_bp.route('/test3/')
def test3():
    import time

    print("Printed immediately.")
    time.sleep(1.4)
    return "Hello from test3"

@contact_bp.route('/test4/')
def test4():
    return "Hello from test4"