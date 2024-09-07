
# Proyecto de Conexión Cliente-Servidor con Sockets en Python

## Descripción
Este proyecto implementa una conexión simple entre un cliente y un servidor utilizando sockets TCP/IP. El servidor escucha conexiones en un puerto específico y acepta solicitudes de clientes en la misma red local. Ambos pueden intercambiar mensajes una vez que se establece la conexión.

## Requisitos
- Python 3.x
- Conexión a la misma red local para el cliente y servidor
- Asegúrate de que el puerto que se utilice esté libre y permitido por el firewall

## Instalación
1. Clona el repositorio o descarga los archivos del proyecto.
2. Asegúrate de tener Python instalado.
3. Configura la IP correcta en `cliente.py` para que apunte al servidor.

## Uso

### 1. Ejecutar el Servidor
Primero, inicia el servidor en una máquina en la red local:

```bash
python servidor.py
```

El servidor comenzará a escuchar en la IP y el puerto especificado. Asegúrate de que el servidor esté en ejecución **antes** de que el cliente intente conectarse.

### 2. Ejecutar el Cliente
En otra máquina dentro de la misma red, ejecuta el cliente para conectarte al servidor:

```bash
python cliente.py
```

Especifica la dirección IP del servidor en `cliente.py`. Una vez conectado, puedes enviar mensajes al servidor y recibir respuestas.

## Ejemplo de ejecución

### Servidor
```bash
Servidor escuchando en 0.0.0.0:12345...
Conexión establecida con ('192.168.18.103', 54321)
Cliente: ¡Hola servidor!
```

### Cliente
```bash
Conectado al servidor 192.168.18.102:12345
Tú: ¡Hola servidor!
Servidor: Mensaje recibido por el servidor
```

## Problemas comunes
### Error: `Address already in use`
Este error ocurre cuando el puerto que estás intentando usar ya está en uso. Puedes resolverlo cambiando de puerto o liberando el puerto con:

```bash
sudo lsof -i :12345
sudo kill -9 <PID>
```

### Error: `Connection refused`
Asegúrate de que el servidor esté corriendo y que el puerto esté abierto.