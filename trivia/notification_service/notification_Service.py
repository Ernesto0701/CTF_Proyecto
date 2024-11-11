from flask import Flask, jsonify, request
import time

app = Flask(__name__)

@app.route('/api/notificar', methods=['POST'])
def notificar():
    datos = request.get_json()
    mensaje = datos.get("mensaje")
    jugador = datos.get("jugador")
    
    # Simulación de notificación (por ejemplo, a través de WebSocket o alguna cola de mensajes)
    time.sleep(1)  # Simulando retraso
    return jsonify({"mensaje": f"Notificación enviada a {jugador}: {mensaje}"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
