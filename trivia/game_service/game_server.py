from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Simulación de sesiones de juego
sesiones = {}

@app.route('/api/jugar', methods=['POST'])
def iniciar_juego():
    datos = request.get_json()
    nombre_jugador = datos.get("jugador")
    if nombre_jugador not in sesiones:
        sesiones[nombre_jugador] = {"puntaje": 0, "ronda": 1}
    return jsonify({"mensaje": f"Juego iniciado para {nombre_jugador}", "ronda": 1, "puntaje": 0})

@app.route('/api/responder', methods=['POST'])
def responder_pregunta():
    datos = request.get_json()
    jugador = datos.get("jugador")
    respuesta = datos.get("respuesta")
    
    if jugador not in sesiones:
        return jsonify({"mensaje": "Jugador no encontrado"}), 404
    
    if respuesta == "correcta":  # Aquí agregarías la lógica para verificar la respuesta
        sesiones[jugador]["puntaje"] += 10  # Sumar puntos si la respuesta es correcta
    sesiones[jugador]["ronda"] += 1
    
    return jsonify({"mensaje": "Respuesta recibida", "puntaje": sesiones[jugador]["puntaje"], "ronda": sesiones[jugador]["ronda"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
