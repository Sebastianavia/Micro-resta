
"""
Created on Mon Apr  6 15:07:08 2020

@author: santoyo-yo Cristan Patiño
"""
from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, origins='*')

@app.route('/api/resta', methods=['POST'])
def resta():    
    
    n1 = int(request.get_json()['n1'])
    n2 = int(request.get_json()['n2'])
    result = n1-n2    
    
    return str(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='4040')




curl -X POST -H "Content-Type: application/json" -d '{"n1": 10, "n2": 5}' http://calculadora/resta/api/resta

192.168.49.2  

curl --resolve "calculadora:80:$( minikube ip )" -i http://calculadora
