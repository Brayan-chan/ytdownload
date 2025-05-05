from flask import Flask, request, jsonify, render_template, send_from_directory, redirect, url_for
import yt_dlp
import os

app = Flask(__name__)

# Crear la carpeta "offline" si no existe
if not os.path.exists('offline'):
    os.makedirs('offline')

# Función para descargar un video de YouTube
def descargar_video(url):
    # Configuración de la descarga
    ydl_opts = {
        'format': 'best',  # Calidad del video
        'outtmpl': 'offline/%(title)s.%(ext)s',  # Nombre del archivo de salida
        'restrictfilenames': True,  # Evitar caracteres especiales en el nombre del archivo
    }

    # Crear un objeto yt_dlp
    ydl = yt_dlp.YoutubeDL(ydl_opts)

    # Descargar el video
    try:
        ydl.download([url])
        return f"Video descargado con éxito: {url}"
    except Exception as e:
        return f"Error al descargar el video: {e}"

# Ruta para la página de inicio
@app.route('/')
def index():
    # Obtener la lista de archivos descargados
    archivos_descargados = os.listdir('offline')
    return render_template('index.html', archivos_descargados=archivos_descargados)

# Ruta para subir un archivo
@app.route('/subir', methods=['POST'])
def subir():
    if 'archivo' not in request.files:
        return redirect(url_for('index'))
    archivo = request.files['archivo']
    if archivo.filename == '':
        return redirect(url_for('index'))
    archivo.save(os.path.join('offline', archivo.filename))
    return redirect(url_for('index'))

# Ruta para descargar un video
@app.route('/descargar', methods=['POST'])
def descargar():
    url = request.form['url']
    resultado = descargar_video(url)
    return jsonify({'resultado': resultado})

# Ruta para servir los archivos descargados
@app.route('/offline/<path:path>')
def send_file(path):
    return send_from_directory('offline', path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)