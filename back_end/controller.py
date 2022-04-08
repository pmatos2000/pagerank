from flask import Flask, request, jsonify

from listar_pagina_service import listar_pagina_service

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/busca")
def hello_world():
    busca = request.args.get('busca', default = "", type = str)
    resultado = listar_pagina_service(busca)
    return jsonify(resultado)

app.run()