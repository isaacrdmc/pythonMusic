from pytubefix import Playlist
from pytubefix.cli import on_progress
import os

# TODO: Archivo para poder descargar canciones por lista


url = "https://music.youtube.com/playlist?list=PLo1bJn-s98kSarxkDkpgsVjyUCZSb-92f&si=4V0QPF9pMRcJJT41"
directorio = 'C://Users//isaac//Music//ConPython'


# ? Sección para poder descar música por listas


try:
    # Verificamso si el directorio existe:
    if not os.path.exists(directorio):
        os.makedirs(directorio)

    # La url la hacemos una variable para manipular el contenido
    listaMusic = Playlist(url)
    print(f'Descargando la playList: {listaMusic.title}')

    # Creamos un subdirectorio para la playlist:
    nuevoDirectorio = os.makedirs(directorio, listaMusic.title)


    if not os.path.exists(nuevoDirectorio):
        os.makedirs(nuevoDirectorio)  # Creamos la carpeta de la playlist


    # Recorremos los videos de la play list
    for canciones in listaMusic.videos:
        print(f'Descargando: {canciones.title}')


        # Filtramos el contenido de cada ciclo para obtener solo el audio
        archivo =  canciones.streams.filter(only_audio=True).first()
        
        
        # Si no arroja error entonces descargamos el archivo en la ruta del directorio
        if archivo:
            archivo.download(output_path=nuevoDirectorio)
        else:
            print(f"⚠ No se encontró un stream de audio para {canciones.title}")

except Exception as error:
    print(f"❌ Error al descargar la playlist: {error}")






# url = ""
# directorio = 'C://Users//isaac//Music//ConPython'

# # ? Sección para poder descargar música por listas
# listaMusic = Playlist(url)
# for video in listaMusic.videos:
#     audio_stream = video.streams.filter(only_audio=True).first()
#     if audio_stream:
#         audio_stream.download(output_path=directorio)