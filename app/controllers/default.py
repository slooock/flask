from app import app
# from flask import request
# from flask import jsonify
from app.controllers.process import process
from flask import request
from flask import jsonify

@app.route("/process/default", methods=['GET'])
def getProcess():
    resposta = process.processPost()

    return jsonify(resposta)

@app.route("/process", methods=['POST'])
def postProcess():
    data = request.get_json()["facts"]

    resposta = process.processPost(data)
    return jsonify(resposta)