# Cliente Pyro para Descarga Remota de Videos de YouTube

Este cliente se conecta a un servidor Pyro en otra máquina de la red local para descargar videos de YouTube de forma remota utilizando `yt_dlp`.

## 📁 Estructura del Proyecto

```
CLIENTE_PYRO/
├── app.py          # Cliente Pyro
└── README.md       # Instrucciones
```

## ⚙️ Requisitos

- Python 3.x
- Pyro4

## 🔧 Instalación

1. Clona este repositorio o descarga este ZIP.
2. Crea un entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate    # Windows
   ```

3. Instala Pyro4:
   ```bash
   pip install Pyro4
   ```

## 🚀 Uso

1. Asegúrate de que el **servidor esté corriendo** y tenga esta IP local: `192.168.1.13`
2. En el cliente, ejecuta:

   ```bash
   python app.py
   ```

3. Ingresa la URL del video de YouTube cuando se te solicite.

## 🧠 Notas

- Ambos dispositivos deben estar en la **misma red local**.
- El servidor debe tener corriendo el Name Server (`Pyro4.naming`) y el objeto registrado bajo el nombre `youtube.descargador`.

