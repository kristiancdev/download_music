from pytube import YouTube
import os

# Definir la ruta al archivo de texto con las URL
archivo_url = "lista_urls.txt"

# Definir la ruta de la carpeta de descarga
ruta_descarga = "tu/ruta/de/descarga"

def descargar_video(url):
    try:
        # Crear una instancia de YouTube con la URL
        yt = YouTube(url)

        # Seleccionar la corriente de audio
        stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

        # Descargar el video en la ruta de descarga especificada
        stream.download(output_path=ruta_descarga)

        # Borrar la URL del archivo
        with open(archivo_url, 'r') as file:
            lines = file.readlines()
        with open(archivo_url, 'w') as file:
            for line in lines:
                if line.strip("\n") != url:
                    file.write(line)

        print(f"Descargado: {yt.title}")
    except Exception as e:
        print(f"No se pudo descargar la URL {url}. Error: {str(e)}")

# Abrir el archivo de texto y descargar las URLs
with open(archivo_url, 'r') as file:
    urls = file.readlines()
    for url in urls:
        descargar_video(url.strip("\n"))
