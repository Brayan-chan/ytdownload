
# Descargador de Videos vía Web y RMI con Pyro4

Este proyecto permite descargar videos de YouTube desde una interfaz web usando `yt-dlp`, implementando una arquitectura cliente-servidor con **RMI (Remote Method Invocation)** a través de **Pyro4**.

---

## 📦 Requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- Python 3.8 o superior
- `pip` (Python package installer)
- Acceso a dos terminales

---

## 📁 Instalación

1. Clona este repositorio o copia los archivos del proyecto en una carpeta local.
2. Abre una terminal y navega a esa carpeta.
3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

---

## 📚 `requirements.txt`

Incluye:

```text
Pyro4
yt-dlp
Flask
```

Puedes crearlo con ese contenido o generarlo automáticamente con:

```bash
pip freeze > requirements.txt
```

---

## 🚀 Ejecución del Proyecto

### Paso 1: Iniciar el NameServer de Pyro (Terminal 1)

```bash
pyro4-ns
```

Esto inicia el **NameServer**, un componente central que permite que los clientes encuentren servicios disponibles.

> ❗ Debes dejar esta terminal abierta mientras todo el sistema esté en uso.

---

### Paso 2: Iniciar el Servidor Pyro (Terminal 2)

Abre otra terminal (nueva ventana o pestaña) y ejecuta:

```bash
python pyro_server.py
```

Esto iniciará el servidor remoto que descargará los videos cuando la app Flask se lo solicite mediante RMI.

---

### Paso 3: Iniciar la aplicación web Flask (Terminal 3)

Opcionalmente, en una tercera terminal puedes ejecutar:

```bash
python app.py
```

Esto levantará un servidor web en: [http://localhost:5001](http://localhost:5001)

---

## 🌐 Uso desde el Navegador

1. Abre tu navegador en [http://localhost:5001](http://localhost:5001)
2. Verás una interfaz para:
   - Ingresar la URL del video de YouTube
   - Descargarlo usando el servidor Pyro
   - Ver los archivos ya descargados
   - Subir archivos manualmente a la carpeta `offline`

---

## 🧠 ¿Cómo funciona?

- El usuario ingresa una URL en la interfaz web.
- Flask se conecta al servidor Pyro usando `Pyro4.Proxy(...)`.
- El servidor Pyro ejecuta `yt_dlp` para descargar el video y lo guarda en la carpeta `offline`.
- Flask muestra la lista de archivos disponibles desde esa carpeta.

---

## 📁 Estructura del Proyecto

```
.
├── pyro_server.py        # Servidor remoto Pyro4
├── app.py                # Aplicación web Flask
├── templates/
│   └── index.html        # Interfaz web
├── offline/              # Carpeta donde se guardan los videos
├── requirements.txt
└── README.md             # Este archivo
```

---

## 🔒 Consideraciones de Seguridad

- Esta aplicación no tiene autenticación. No debe exponerse a internet sin protección.
- Evita exponer tu servidor Pyro a redes públicas sin filtros de acceso.

---

## 🧪 Pruebas y depuración

Si ves errores como `Cannot connect to Name Server`, asegúrate de:

- Que el **Name Server esté activo** (`pyro4-ns`).
- Que las IPs en `pyro_server.py` y en el cliente coincidan con tu red local.
- Que el firewall no esté bloqueando puertos.

---

## 🤝 Autor

Proyecto realizado como práctica de RMI usando Pyro4 y Flask.

---
