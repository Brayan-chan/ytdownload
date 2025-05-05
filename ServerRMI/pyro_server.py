import Pyro4
import yt_dlp
import os

# Asegúrate de que la carpeta "offline" exista
if not os.path.exists("offline"):
    os.makedirs("offline")

@Pyro4.expose
class Descargador:
    def descargar_video(self, url):
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'offline/%(title)s.%(ext)s',
            'restrictfilenames': True,
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            return "Video descargado con éxito"
        except Exception as e:
            return f"Error: {str(e)}"

# Crear el demonio y registrar el objeto
daemon = Pyro4.Daemon(host="192.168.1.13")  # IP de tu PC (el servidor)

uri = daemon.register(Descargador)
print(f"URI del servidor: {uri}")

# Registrar en el nameserver
ns = Pyro4.locateNS()
ns.register("descargador.youtube", uri)

print("Servidor Pyro corriendo...")
daemon.requestLoop()
