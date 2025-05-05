from flask import Flask, request, render_template
import Pyro4

app = Flask(__name__)

# Configura la IP del servidor Pyro
Pyro4.config.NS_HOST = "192.168.1.13"  # Cambia esta IP si tu servidor está en otra dirección
descargador = Pyro4.Proxy("PYRONAME:descargador.youtube")

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            try:
                resultado = descargador.descargar_video(url)
            except Exception as e:
                resultado = f"Error al contactar al servidor: {str(e)}"
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
