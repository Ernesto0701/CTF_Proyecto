from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulación de base de datos de usuarios
usuarios = {}

@app.route('/api/registro', methods=['POST'])
def registrar_usuario():
    datos = request.get_json()
    nombre_usuario = datos.get("usuario")
    if nombre_usuario in usuarios:
        return jsonify({"mensaje": "Usuario ya existe"}), 400
    usuarios[nombre_usuario] = {"nivel": 1, "puntaje_total": 0}
    return jsonify({"mensaje": f"Usuario {nombre_usuario} registrado correctamente"})

@app.route('/api/perfil/<string:usuario>', methods=['GET'])
def obtener_perfil(usuario):
    if usuario not in usuarios:
        return jsonify({"mensaje": "Usuario no encontrado"}), 404
    return jsonify(usuarios[usuario])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
