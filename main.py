from flask import Flask, request, jsonify
import json
import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=MARCELOPC;'
                      'Database=estudo;'
                      'Trusted_Connection=yes;')

app = Flask(__name__)

nomes = [
    {"nome":"Marcelo", "idade":29},
    {"nome":"Teste 2", "idade":25},
    {"nome":"Teste 3", "idade":18},
]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)



@app.route('/foo', methods=['POST'])
def foo():
    data = request.json
    print(data)
    return jsonify(data)

@app.route("/ola", methods=['GET'])
def ola():
    return jsonify(nomes)

@app.route("/db", methods=['GET'])
def getData():
    data = []
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuario')
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        result = dict(zip(columns, row))
        results.append(result)
    return jsonify(results)


'''
    set FLASK_APP=main.py
    set FLASK_RUN_PORT=8000
    set FLASK_RUN_HOST=192.168.0.50 
    flask run
    py -m venv venv
'''