# -*- coding: utf-8 -*-
import os
import sys
import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask.cli import AppGroup

app = Flask(__name__)
api = Api(app)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

from models.beer import *
from models.ingredient import *
from models.location import *
from models.locationview import *

migrate = Migrate(app, db)

from controllers.index import *
from controllers.beercontroller import *
from controllers.locationcontroller import *

api.add_resource(Index, '/')
# GET all beers
api.add_resource(BeersController, '/example/rest/v1/beers')
# GET, PUT and DELETE one beer by id
api.add_resource(BeerControllerById, '/example/rest/v1/beer/<int:id>')
# POST beer (Create beer or new beer)
api.add_resource(BeerController, '/example/rest/v1/beer')

# GET one location by id
api.add_resource(LocationControllerById, '/example/rest/v1/location/<int:id>')

from seeders.dataseed import DataSeed


@app.cli.command("seed")
def create_data():
    """
        Define seed command, run in terminal:
        $ flask seed
    """
    DataSeed.create()


from views.viewlocation import ViewLocation

view_cli = AppGroup('view')


@view_cli.command("create")
def create_view():
    """
        Create view:
        $ flask view create
    """
    ViewLocation.create()


@view_cli.command("drop")
def drop_view():
    """
        Drop view:
        $ flask view drop
    """
    ViewLocation.drop()


app.cli.add_command(view_cli)


@app.errorhandler(404)
def invalid_route(e):
    """
        Define custom 404 in json when not exist route
    """
    app.logger.error('Route not found')
    return jsonify({
        'message': 'Route not found'
    }), 404


# Logger
filename = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                        'logs',
                        'server.log')
logging.basicConfig(level=logging.DEBUG,
                    format="[%(levelname)s] %(asctime)s %(message)s",
                    handlers=[
                        logging.FileHandler(filename),
                        logging.StreamHandler(sys.stdout)
                    ])
app.logger.info('Start Flask Server')
