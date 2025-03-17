#Grupo: Keidys Salguedo y Rafael Mantilla

from flask import Flask, request, jsonify
app = Flask(__name__)

#Ruta que responde a la solicitud GET del endpoint para devolver una lista de personas 
@app.route('/api/personas', methods= ['GET'])
def index():
    #Lista de personas que devuelve el endpoint en formato JSON 
    lista_personas = [
        {'name': 'Keidys Salguedo', 'age': 20},
        {'name': 'Rafael Mantilla', 'age': 21},
        {'name': 'Margarita Ortega', 'age': 24},
        {'name': 'Carlos Monsalve', 'age': 30}
    ]
    #Convierte la lista en un JSON y lo devuelve con un codigo 200 que se refiere al metodo GET
    return jsonify(lista_personas), 200

if __name__ == '__main__':
    #Inicializa la aplicacion con un debug activado
    app.run(debug= True)

# Lo que hace este codigo es crear un endpoint que responde a la solicitud GET /api/personas, para asi devolver una lista de personas que ya estan definidas de forma estatica 
