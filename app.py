from flask import Flask, request, jsonify
from flask_restful import Api
from resources.knn import Make_predict
import pickle

app = Flask(__name__)

api = Api(app)

api.add_resource(Make_predict, '/knn')

app.run(port=5017)
