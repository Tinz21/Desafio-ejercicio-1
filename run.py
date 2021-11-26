# Flask
from flask import Flask, request, json
# Service
from app.service.PatentesService import PatentesService
from app.service.PatentesService import IdService

app = Flask(__name__)

# Endpoint que ingresa patente y retorna el id asociado
@app.route('/patentes')
def code():
    patente_code = request.args.get('code')
    id = PatentesService(patente_code).find_letter_position()
    response = app.response_class(
        response=json.dumps({
            "id": id
        }),
        status=200,
        mimetype='application/json'
    )
    return response

#  Endpoint que ingresa el id y retorna la patente
@app.route('/idpatente')
def id_patente():
    id = request.args.get('id')
    patente = IdService(id).find_code()
    response = app.response_class(
        response = json.dumps({
            "patente":patente
        }),
        status = 200,
        mimetype = 'application/json'
    )
    return response
    

if __name__=='__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)