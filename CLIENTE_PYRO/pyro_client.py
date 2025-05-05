import Pyro4

Pyro4.config.NS_HOST = "192.168.1.13"  # IP del servidor
descargador = Pyro4.Proxy("PYRONAME:descargador.youtube")

url = input("Pega la URL del video de YouTube: ")
resultado = descargador.descargar_video(url)
print("Resultado:", resultado)
