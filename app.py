import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db') #If Database_url not found, we will use postgre uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #This will stop the SQL_Alchemy's object change tracking, since the same is also taken care of by Flask_SQL_Alchemy
app.secret_key='munjal'
api=Api(app)


jwt=JWT(app, authenticate, identity) 
#JWT creates new endpoint /auth which will call authenticate and identity func of security.py
#it will then return jwt token which will be used in subsequent requests


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')    
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')


if __name__ == '__main__': 
    #All things under this will only run when this file is exeuted and not when imported
    from db import db #Imported here to prevent circular importing
    db.init_app(app)
    app.run(port=5000, debug=True)
