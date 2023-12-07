from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from os import path
from .databases.init_db import *
from .databases.CRUD_bus_stop import *
from .passengers import passengers_on_stops
from .data_values_initialization import *
# from flask_login import LoginManager


"""
Инициализируется всегда, когда программа открывает папку website
"""

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dsavmfdsoqwevp'
    """ЗАМЕНИТЬ НА НОРМ ДБ"""
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # db.init_app(app)

    from .views import views
    # from .views_old import views_old

    # авторизация человека
    # from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    # app.register_blueprint(auth, url_prefix='/')

    # create_databases(app)
    db.create_tables([BusStop, Bus, Driver, Route, BusTrip, PathPoint, RoutePath])
    init_path_points()
    init_bus_stops()

    dict_stops = passengers_on_stops(get_bus_stop_all())
    print(dict_stops)
    update_bus_stop_all(dict_stops)
    
    return app


# def create_databases(app):
    # if not path.exists('website/' + DB_NAME):
    #     with app.app_context():
    #         db.create_all()
    #     print('Created Database!')
