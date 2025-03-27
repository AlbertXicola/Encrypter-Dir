# Kichola Malware v1.0 - README

Bienvenido a **Kichola Malware v1.0**, una herramienta poderosa y dinámica para encriptación y desencriptación de archivos. A continuación, se explica el funcionamiento de la aplicación, el manejo de la clave de encriptación y consideraciones importantes.

---

## **Descripción del Programa**

**Kichola Malware v1.0** es un programa de línea de comandos que permite:
1. Ver información detallada del sistema.
2. Encriptar archivos dentro de un directorio específico.
3. Desencriptar archivos previamente encriptados utilizando una clave de encriptación.

El software está diseñado para ser ejecutado como un archivo **.exe** en Windows o Linux.

---

## **Flujo de Trabajo**

### 1. **Mostrar Información del Sistema**
Al seleccionar la opción para mostrar la información del sistema, el programa proporcionará los siguientes detalles:
- Sistema Operativo
- Versión del sistema operativo
- Procesador
- Memoria RAM total
- Núcleos físicos y lógicos

### 2. **Encriptar Archivos**
El usuario puede encriptar archivos en un directorio específico. Durante este proceso:
- El programa recorrerá todos los archivos del directorio y los encriptará.
- **Importante**: **La clave de encriptación será eliminada automáticamente después de completar la encriptación**. 
- **Asegúrate de copiar la clave antes de que se elimine**.

**Advertencia en rojo**:
```diff
- ¡Asegúrate de copiar la clave de encriptación antes de que se elimine!
