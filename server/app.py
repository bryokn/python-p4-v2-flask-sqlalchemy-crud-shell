# server/app.py

'''from flask import Flask
from flask_migrate import Migrate

from models import db, Pet

# create a Flask application instance 
app = Flask(__name__)

# configure the database connection to the local file app.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# configure flag to disable modification tracking and use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create a Migrate object to manage schema modifications
migrate = Migrate(app, db)

# initialize the Flask application to use the database
db.init_app(app)

@app.route('/')
def index():
    pets = Pet.query.all()
    pet_list = ''
    for pet in pets:
        pet_list += f'{pet.name} ({pet.species})<br>'
    return pet_list

if __name__ == '__main__':
    app.run(port=5555, debug=True)
'''

# server/app.py

from flask import Flask
from flask_migrate import Migrate

from models import db, Pet

# create a Flask application instance 
app = Flask(__name__)

# configure the database connection to the local file app.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# configure flag to disable modification tracking and use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create a Migrate object to manage schema modifications
migrate = Migrate(app, db)

# initialize the Flask application to use the database
db.init_app(app)

@app.before_first_request
def initialize_database():
    if not Pet.query.first():
        pet1 = Pet(name='Bosco', species='Dog')
        pet2 = Pet(name='Daisy', species='Cat')
        pet3 = Pet(name='Kasuku', species='Bird')
        db.session.add_all([pet1, pet2, pet3])
        db.session.commit()

@app.route('/')
def index():
    pets = Pet.query.all()
    pet_list = ''
    for pet in pets:
        pet_list += f'{pet.name} ({pet.species})<br>'
    return pet_list

if __name__ == '__main__':
    app.run(port=5555, debug=True)