from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id':'0', 
        'nome':'Rayrison',
        'habilidades':['Python', 'Flask']
    },
    {
        'id':'1',
        'nome':'Lima',
        'habilidades':['Python', 'Django']
    }
]

class Desenvolvedor(Resource):
    def get(self):
        return {'nome':'Rayrison'}

    def put(self):
        pass
    
    def delete(self):
        pass

api.add_resource(Desenvolvedor, '/dev/')

if __name__ == '__main__':
    app.run(debug=True)