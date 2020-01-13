from flask import Flask
from flask_restful import Api

from resources.pythonapi import PythonAPI

app = Flask(__name__)
api = Api(app)

api.add_resource(PythonAPI, "/api/<str:val>")

if __name__ == "__main__":
  app.run()