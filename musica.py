from pytubefix import YouTube
from pytubefix.cli import on_progress
import os


# TODO: Archivo para poder descargar canciones de una en una

# url = str(input('Ingresa la URL de la conación a descargar: \n>>'))
# directorio = input('Ingresa el directorio para guardar el archivo')

url = "https://youtu.be/qpCNaRkIh2E?si=Cxa9xO6Hgr579v-Z"
directorio = 'C://Users//isaac//Music//ConPython'



try:
    # Verificamos si el directorio de descargas existe:
    if not os.path.exists(directorio):
        os.makedirs(directorio) # Creamos el directorio si no existe

    # ? Extraemos lo que encesitamos de la URL:
    yt = YouTube(url, on_progress_callback=on_progress)
    print(f'Descargando: {yt.title}')

    # ? Extraemos unicamente el audio (En este caso)
    archivo = yt.streams.filter(only_audio=True).first()

    # ^
    # ? Descargamos el archivo
    resultadoDescarga = archivo.download(output_path=directorio)

    # * Cambiamos la extención a '.mp3'
    base, ext = os.path.splitext(resultadoDescarga)
    nuevaDescarga = base + '.mp3'

    # Verificamos si el archivo ya existe antes de renombrar
    if os.path.exists(nuevaDescarga):
        print(f'El archivo {nuevaDescarga} ya existe.')
    else:
        os.rename(
            resultadoDescarga,  # La ruta donde se descargo el archivo
            nuevaDescarga   # El archivo más la extencion '.mp3'
        )
        print(f'{yt.title} fue descargado correcctamente en {nuevaDescarga}')

except Exception as error:
    print(f'Hay un error al descargar el video: {str(error)}')



