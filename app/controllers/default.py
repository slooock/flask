from app import app
# from flask import request
# from flask import jsonify
from app.controllers.process import process

@app.route("/process/default", methods=['GET'])
def getProcess():
    resposta = process.process()

    return str(resposta)