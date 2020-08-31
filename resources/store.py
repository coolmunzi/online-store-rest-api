from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        else:
            return {'message': '{} store was not found.'.format(name) }, 400


    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': '{} store already exists'.format(name)}, 400
        
        store=StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'Error inserting store data'}, 500
        
        return store.json(), 200   


    def delete(self, name):
        store=StoreModel.find_by_name(name)
        if store:
            try:
                store.delete_from_db()
            except:
                return {'message':'Error deleting store data'}, 500
      
            return {'message': '{} store is deleted'.format(name)}
        return {'message': '{} store is not found'.format(name)}
        

class StoreList(Resource):
    def get(self):
        return {'stores': [store.json for store in StoreModel.query.all()]}
