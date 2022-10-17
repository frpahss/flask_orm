from flask import Flask
# from models import db


def create_app():
    app_flask = Flask(__name__)

    # Datenbank
    app_flask.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webshop.sqlite'
    app_flask.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # db.init_app(app_flask)

    return app_flask


app = create_app()

with app.app_context():
    print('Hier in app.app_context()')
    # db.drop_all()
    # db.create_all()


@app.route('/')
def index():
    return ('<h1>ORM Tutorial</h1>')


app.run(debug=True)
