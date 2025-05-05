
# Cliente Pyro para Descargar Videos de YouTube (con Interfaz Web)

Este cliente se conecta al servidor Pyro que descarga videos desde YouTube utilizando `yt-dlp`, y ahora incluye una **interfaz web moderna con Flask** para ingresar la URL del video.

---

## 📁 Estructura del Proyecto (Cliente)

```
.
├── pyro_client.py        # Lógica para conectar con el servidor Pyro
├── web_client.py         # Flask app que usa pyro_client desde la web
├── templates/
│   └── index.html        # Interfaz de usuario HTML
├── requirements.txt      # Dependencias necesarias
└── README.md             # Este archivo
```

---

## ⚙️ Requisitos

- Python 3.8 o superior
- pip
- Acceso al servidor Pyro (debe estar corriendo)
- Flask y Pyro4 instalados

---

## 🔧 Instalación

1. Asegúrate de que el servidor Pyro esté corriendo (ver su README).
2. Clona este repositorio o copia los archivos del cliente.
3. Instala las dependencias con:

```bash
pip install -r requirements.txt
```

---

## 🚀 Ejecución

### 1. Iniciar la interfaz web (cliente Flask)

```bash
python web_client.py
```

Esto ejecutará la app en [http://localhost:5002](http://localhost:5002)

### 2. Usar desde el navegador

- Abre [http://localhost:5002](http://localhost:5002)
- Pega la URL del video de YouTube
- Presiona **Descargar**
- El resultado aparecerá en pantalla

---

## 📝 requirements.txt sugerido

```
Flask
Pyro4
```

---

## 🧠 Funcionamiento

- El usuario ingresa una URL en el formulario HTML.
- Flask recoge la URL y llama al servidor Pyro con `Pyro4.Proxy(...)`.
- El servidor descarga el video y devuelve un mensaje de éxito o error.
- La interfaz muestra el resultado al usuario.

---

## 🛡️ Notas

- Asegúrate de que la IP del servidor esté correctamente definida en `web_client.py`.
- Si el servidor está en otra máquina, habilita los puertos necesarios (por defecto Pyro usa 9090+).
