from flask import Flask

from src.common.database import Database

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = "123"


@app.before_first_request
def init_db():
    print("in initialize")
    Database.initialize()
    user = Database.find_one("users", {"email": "test@test.com"})
    print("user from db: ", user)


@app.route('/')
def home():
    return "Hello"


from src.models.users.views import user_blueprint

app.register_blueprint(user_blueprint, url_prefix="/users")
