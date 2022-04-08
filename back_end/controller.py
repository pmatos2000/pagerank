from flask import Flask, request, jsonify
from flask_cors import CORS

from listar_pagina_service import listar_pagina_service

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config['JSON_AS_ASCII'] = False
app.config['CORS_HEADERS'] = 'application/json'


@app.route("/busca")
def busca():
    busca = request.args.get('busca', default = "", type = str)
    resultado = listar_pagina_service(busca)
    return jsonify(resultado)


app.run()