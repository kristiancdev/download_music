# Descargador de Música desde YouTube

Este script de Python permite descargar música desde YouTube a partir de una lista de URLs contenidas en un archivo de texto.

## Requisitos

Antes de utilizar este script, asegúrate de tener instalada la biblioteca `pytube`. Puedes instalarla con el siguiente comando:

```bash
pip install pytube
```

### Uso

1. Coloca las URLs de los videos de YouTube que desees descargar en un archivo de texto llamado lista_urls.txt, una URL por línea.

2. Abre el archivo download_music.py y modifica la variable ruta_descarga para especificar la carpeta donde deseas guardar las descargas.

3. Ejecuta el script download_music.py:

```bash
python download_music.py
```

El script leerá las URLs del archivo lista_urls.txt, descargará el audio de cada video de YouTube y eliminará la URL del archivo una vez completada la descarga.

Personalización
Puedes personalizar este script según tus necesidades. Por ejemplo, puedes agregar opciones para seleccionar la calidad de audio o el formato de salida.

Contribuciones
Si encuentras errores o mejoras posibles en este script, siéntete libre de contribuir. Abre un problema o envía una solicitud de extracción.

**_KristiancDev_**
