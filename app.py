from flask import Flask, request, jsonify, render_template
import yt_dlp

app = Flask(__name__)

# Función para descargar un video de YouTube
def descargar_video(url):
    # Configuración de la descarga
    ydl_opts = {
        'format': 'best',  # Calidad del video
        'outtmpl': '%(title)s.%(ext)s',  # Nombre del archivo de salida
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
    return render_template('index.html')

# Ruta para descargar un video
@app.route('/descargar', methods=['POST'])
def descargar():
    url = request.form['url']
    resultado = descargar_video(url)
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)