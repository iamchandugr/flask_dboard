from flask import Flask
import flask_monitoringdashboard as dashboard
from home import home_bp
from contact import contact_bp

app = Flask(__name__)

app.register_blueprint(home_bp, url_prefix='/home')
app.register_blueprint(contact_bp, url_prefix='/contact')
dashboard.config.init_from(file='/Users/chandraseker/learn/flask_dashboard/venv/config.cfg')
dashboard.bind(app)
@app.before_request
def before():
    print("This is executed BEFORE each request.")

app.run()