from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulación de base de datos de preguntas
preguntas = [
    {"id": 1, "categoria": "Ciencia", "pregunta": "¿Cuál es el elemento químico con el símbolo H?", "respuesta": "Hidrógeno", "dificultad": "Fácil"},
    {"id": 2, "categoria": "Historia", "pregunta": "¿Quién fue el primer presidente de los Estados Unidos?", "respuesta": "George Washington", "dificultad": "Fácil"},
    {"id": 3, "categoria": "Geografía", "pregunta": "¿En qué continente se encuentra Egipto?", "respuesta": "África", "dificultad": "Media"},
]

@app.route('/api/preguntas', methods=['GET'])
def obtener_preguntas():
    # Devuelve todas las preguntas
    return jsonify(preguntas)

@app.route('/api/pregunta/<int:id>', methods=['GET'])
def obtener_pregunta(id):
    # Devuelve una pregunta por su ID
    pregunta = next((p for p in preguntas if p["id"] == id), None)
    if pregunta:
        return jsonify(pregunta)
    return jsonify({"mensaje": "Pregunta no encontrada"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
