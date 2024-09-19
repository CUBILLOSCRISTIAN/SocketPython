## Proyecto de Comunicación Segura con Cifrado

Este proyecto implementa un sistema de comunicación segura entre un cliente y un servidor utilizando dos métodos de cifrado diferentes: Salsa20 y AES-256-CBC. El proyecto consta de cuatro scripts principales:

1. `CLIENTE_SALSA_20.PY`
2. `SERVIDOR_SALSA_20.PY`
3. `CLIENTE_AES.PY`
4. `SERVIDOR_AES.PY`

### Descripción de los Scripts

#### CLIENTE_SALSA_20.PY

Este script implementa un cliente que se conecta a un servidor utilizando sockets y cifra los mensajes utilizando el algoritmo Salsa20. El flujo de trabajo es el siguiente:

1. Se conecta al servidor especificado por la IP y el puerto.
2. Recibe una clave simétrica del servidor.
3. En un bucle, el cliente:
   - Toma un mensaje de entrada del usuario.
   - Cifra el mensaje utilizando Salsa20.
   - Envía el mensaje cifrado al servidor.
   - Recibe un mensaje cifrado del servidor.
   - Descifra el mensaje recibido y lo muestra en la consola.
4. La conexión se cierra cuando se recibe el mensaje "adios".

#### SERVIDOR_SALSA_20.PY

Este script implementa un servidor que se comunica con un cliente utilizando sockets y cifra los mensajes utilizando el algoritmo Salsa20. El flujo de trabajo es el siguiente:

1. Escucha conexiones en una IP y puerto especificados.
2. Acepta una conexión entrante de un cliente.
3. Genera una clave simétrica y la envía al cliente.
4. En un bucle, el servidor:
   - Recibe un mensaje cifrado del cliente.
   - Descifra el mensaje recibido y lo muestra en la consola.
   - Toma un mensaje de entrada del usuario.
   - Cifra el mensaje utilizando Salsa20.
   - Envía el mensaje cifrado al cliente.
5. La conexión se cierra cuando se recibe el mensaje "adios".

#### CLIENTE_AES.PY

Este script implementa un cliente que se conecta a un servidor utilizando sockets y cifra los mensajes utilizando el algoritmo AES-256-CBC. El flujo de trabajo es el siguiente:

1. Carga una clave AES desde un archivo.
2. Se conecta al servidor especificado por la IP y el puerto.
3. Cifra un mensaje utilizando AES-256-CBC.
4. Envía el IV y el mensaje cifrado al servidor.

#### SERVIDOR_AES.PY

Este script implementa un servidor que se comunica con un cliente utilizando sockets y cifra los mensajes utilizando el algoritmo AES-256-CBC. El flujo de trabajo es el siguiente:

1. Genera una clave AES y la almacena en un archivo.
2. Escucha conexiones en una IP y puerto especificados.
3. Acepta una conexión entrante de un cliente.
4. Recibe el IV y el mensaje cifrado del cliente.
5. Descifra el mensaje recibido y lo muestra en la consola.

### Requisitos

- Python 3.x
- PyCryptodome (`pip install pycryptodome`)

### Ejecución

1. **Servidor Salsa20**:
   - Ejecutar `SERVIDOR_SALSA_20.PY` en una terminal.
2. **Cliente Salsa20**:
   - Ejecutar `CLIENTE_SALSA_20.PY` en otra terminal.
3. **Servidor AES**:
   - Ejecutar `SERVIDOR_AES.PY` en una terminal.
4. **Cliente AES**:
   - Ejecutar `CLIENTE_AES.PY` en otra terminal.

### Notas

- Asegúrese de que las IPs y puertos especificados en los scripts coincidan y sean accesibles entre el cliente y el servidor.

Este proyecto demuestra cómo implementar comunicación segura utilizando cifrado simétrico en Python.