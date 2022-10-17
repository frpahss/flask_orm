from flask import Flask
from models import db, Team, Member


def create_app():
    app_flask = Flask(__name__)

    # Datenbank
    app_flask.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webshop.sqlite'
    app_flask.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app_flask)

    return app_flask


app = create_app()


def befuellen():
    team_1 = Team("Team - Login")
    team_2 = Team("Team - Katalog")
    db.session.add_all([team_1, team_2])

    member_1 = Member("rita11", "Rita", team_1)
    member_2 = Member("rico2010", "Rico", team_1)
    member_3 = Member("rocco0943", "Rocco", team_1)

    db.session.add_all([member_1, member_2, member_3])

    db.session.commit()

    team_all = Team.query.all()
    for team in team_all:
        print(f'{team.tea_id}: {team.tea_name}')
        for member in team.tea_members:
            print(f'\t{member.mem_id}: {member.mem_name}')


with app.app_context():
    print('Hier in app.app_context()')
    db.drop_all()  # loescht alle tabellen
    db.create_all()  # erstellt alle tabellen neu
    befuellen()


@app.route('/')
def index():
    return ('<h1><b>ORM Tutorial</b></h1>')


app.run(debug=True)
