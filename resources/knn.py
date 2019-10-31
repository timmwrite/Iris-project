from flask_restful import Resource, reqparse
import numpy as np
import pickle
import requests
import model



class Make_predict(Resource):
    def post():
    data = request.get_json(force=True)
    prediction = model.predict([[np.array(data['exp'])]])
    pred = prediction[0]
    return  pred


            

