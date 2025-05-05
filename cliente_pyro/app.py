import Pyro4

def main():
    try:
        # Conéctate al servidor usando la IP del servidor (dispositivo 1)
        ns = Pyro4.locateNS(host="192.168.1.13")  # Cambia si tu servidor tiene otra IP
        uri = ns.lookup("youtube.descargador")
        descargador = Pyro4.Proxy(uri)

        # Pide al usuario la URL
        url = input("Ingresa la URL del video de YouTube: ")
        
        # Llama al método remoto
        resultado = descargador.descargar_video(url)
        print("Respuesta del servidor:", resultado)

    except Exception as e:
        print("Error al conectar con el servidor:", e)

if __name__ == "__main__":
    main()
