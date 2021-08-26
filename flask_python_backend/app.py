from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_cors import CORS
import yaml

app = Flask(__name__)
config = yaml.safe_load(open('database.yaml'))
client = MongoClient(config['uri'])
# db = client.lin_flask
db = client['pront_med']
CORS(app)

@app.route('/')
def index():
    return render_template('home.html')

'''Formulários de Pacientes

Pegar todos os Pacientes e confirmar inscrição'''

@app.route('/api/v1/pac', methods=['POST', 'GET'])
def pacdata():
    
    # POST a data to database
    if request.method == 'POST':
        body = request.json
        nome = body['nome']
        cpf = body['cpf']
        cirurgiao = body['cirurgiao']
        diasInternado = body['diasInternado']
        horasCirurgia = body['horasCirurgia']
        uti = body['uti']
        reservaSangue = body['reservaSangue']
        biopsiaCongelacao = body['biopsiaCongelacao']
        hospital = body['hospital']
        
        # db.users.insert_one({
        db['cirurgias'].insert_one({
            'nome': nome,
            'cpf': cpf,
            'cirurgiao': cirurgiao,
            'diasInternado': diasInternado,
            'horasCirurgia': horasCirurgia,
            'uti': uti,
            'reservaSangue': reservaSangue,
            'biopsiaCongelacao': biopsiaCongelacao,
            'hospital': hospital
        })
        return jsonify({
            'status': 'Data is posted to MongoDB!',
            'nome': nome,
            'cpf': cpf,
            'cirurgiao': cirurgiao,
            'diasInternado': diasInternado,
            'horasCirurgia': horasCirurgia,
            'uti': uti,
            'reservaSangue': reservaSangue,
            'biopsiaCongelacao': biopsiaCongelacao,
            'hospital': hospital
        })
    
    # GET all data from database
    if request.method == 'GET':
        allData = db['cirurgias'].find()
        dataJson = []
        for data in allData:
            id = data['_id']
            nome = data['nome']
            cpf = data['cpf']
            cirurgiao = data['cirurgiao']
            diasInternado = data['diasInternado']
            horasCirurgia = data['horasCirurgia']
            uti = data['uti']
            reservaSangue = data['reservaSangue']
            biopsiaCongelacao = data['biopsiaCongelacao']
            hospital = data['hospital']
            dataDict = {
                'id': str(id),
                'nome': nome,
                'cpf': cpf,
                'cirurgiao': cirurgiao,
                'diasInternado': diasInternado,
                'horasCirurgia': horasCirurgia,
                'uti': uti,
                'reservaSangue': reservaSangue,
                'biopsiaCongelacao': biopsiaCongelacao,
                'hospital': hospital
            }
            dataJson.append(dataDict)
        print(dataJson)
        return jsonify(dataJson)

'''Pegar, deletar e atualizar dados de um paciente'''

@app.route('/api/v1/pac/<string:id>', methods=['GET', 'DELETE', 'PUT'])
def paconedata(id):

    # GET a specific data by id
    if request.method == 'GET':
        data = db['cirurgias'].find_one({'_id': ObjectId(id)})
        id = data['_id']
        nome = data['nome']
        cpf = data['cpf']
        cirurgiao = data['cirurgiao']
        diasInternado = data['diasInternado']
        horasCirurgia = data['horasCirurgia']
        uti = data['uti']
        reservaSangue = data['reservaSangue']
        biopsiaCongelacao = data['biopsiaCongelacao']
        hospital = data['hospital']
        dataDict = {
            'id': str(id),
            'nome': nome,
            'cpf': cpf,
            'cirurgiao': cirurgiao,
            'diasInternado': diasInternado,
            'horasCirurgia': horasCirurgia,
            'uti': uti,
            'reservaSangue': reservaSangue,
            'biopsiaCongelacao': biopsiaCongelacao,
            'hospital': hospital
        }
        print(dataDict)
        return jsonify(dataDict)
        
    # DELETE a data
    if request.method == 'DELETE':
        db['cirurgias'].delete_many({'_id': ObjectId(id)})
        print('\n # Deletion successful # \n')
        return jsonify({'status': 'Data id: ' + id + ' is deleted!'})

    # UPDATE a data by id
    if request.method == 'PUT':
        body = request.json
        nome = body['nome']
        cpf = body['cpf']
        cirurgiao = body['cirurgiao']
        diasInternado = body['diasInternado']
        horasCirurgia = body['horasCirurgia']
        uti = body['uti']
        reservaSangue = body['reservaSangue']
        biopsiaCongelacao = body['biopsiaCongelacao']
        hospital = body['hospital']

        db['cirurgias'].update_one(
            {'_id': ObjectId(id)},
            {
                "$set": {
                    'nome': nome,
                    'cpf': cpf,
                    'cirurgiao': cirurgiao,
                    'diasInternado': diasInternado,
                    'horasCirurgia': horasCirurgia,
                    'uti': uti,
                    'reservaSangue': reservaSangue,
                    'biopsiaCongelacao': biopsiaCongelacao,
                    'hospital': hospital
                }
            }
        )

        print('\n # Update successful # \n')
        return jsonify({'status': 'Data id: ' + id + ' is updated!'})


'''Visualizar os dados de um paciente em específico'''

@app.route('/api/v1/pac/<string:id>/visualizar', methods=['GET'])
def pacview(id):

    # GET a specific data by id
    if request.method == 'GET':
        data = db['cirurgias'].find_one({'_id': ObjectId(id)})
        id = data['_id']
        nome = data['nome']
        cpf = data['cpf']
        cirurgiao = data['cirurgiao']
        diasInternado = data['diasInternado']
        horasCirurgia = data['horasCirurgia']
        uti = data['uti']
        reservaSangue = data['reservaSangue']
        biopsiaCongelacao = data['biopsiaCongelacao']
        hospital = data['hospital']
        dataDict = {
            'id': str(id),
            'nome': nome,
            'cpf': cpf,
            'cirurgiao': cirurgiao,
            'diasInternado': diasInternado,
            'horasCirurgia': horasCirurgia,
            'uti': uti,
            'reservaSangue': reservaSangue,
            'biopsiaCongelacao': biopsiaCongelacao,
            'hospital': hospital
        }
        print(dataDict)
        return jsonify(dataDict)

'''Listar Medicos baseado em um banco pronto'''

@app.route('/api/v1/medicos', methods=['GET'])
def meddata():
    
    # GET all data from database
    if request.method == 'GET':
        allData = db['medicos'].find()
        dataJson = []
        for data in allData:
            id = data['_id']
            nome = data['nome']
            CRM = data['CRM']
            departamento = data['departamento']
            dataDict = {
                'id': str(id),
                'nome': nome,
                'CRM': CRM,
                'departamento': departamento,
            }
            dataJson.append(dataDict)
        print(dataJson)
        return jsonify(dataJson)

'''Listar Hospitais baseados em um banco pronto'''

@app.route('/api/v1/hospitais', methods=['GET'])
def hospdata():
    
    # GET all data from database
    if request.method == 'GET':
        allData = db['hospitais'].find()
        dataJson = []
        for data in allData:
            id = data['_id']
            nome = data['nome']
            endereco = data['endereco']
            cidade = data['cidade']
            dataDict = {
                'id': str(id),
                'nome': nome,
                'endereco': endereco,
                'cidade': cidade,
            }
            dataJson.append(dataDict)
        print(dataJson)
        return jsonify(dataJson)


if __name__ == '__main__':
    app.debug = True
        
    app.run()
