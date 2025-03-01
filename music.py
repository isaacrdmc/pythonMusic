# importing packages
from pytubefix import YouTube
import os

# Ingresar la URL del video como input
yt = YouTube(
    str(input("Ingresa la URL del video que quieres descargar: \n>> ")))

# Extraemos unicamente el audio
video = yt.streams.filter(only_audio=True).first()

# Checamos el destino donde guardar el archvio
print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'

# Descargamos el archivo
out_file = video.download(output_path=destination)

# Guaradamos el archivo
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

# Resultado
print(yt.title + " has been successfully downloaded.")
