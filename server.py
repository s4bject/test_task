from flask import Flask, render_template
from models.models import db, User
from src.api import auth as routes_auth
from flask_login import LoginManager
from config import Config

app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(routes_auth)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'routes_auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)