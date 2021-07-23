from flask import Flask
import flask_monitoringdashboard as dashboard
import pytz # pip install pytz
print(pytz.all_timezones)
app = Flask(__name__)
dashboard.config.init_from(file='/Users/chandraseker/learn/flask_db/venv/config.cfg')
dashboard.bind(app)


@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
  app.run(debug=True)