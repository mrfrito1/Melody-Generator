import mido
import os
from tqdm import tqdm

# Definir la ruta donde se encuentran los archivos MIDI
ruta_midi = "/Users/g.s.e/Desktop/Melody-Generator-1/Melody Generator/midi"

# Inicializar el diccionario de secuencias MIDI
secuencias_midi = {}

# Obtener la lista de archivos MIDI
archivos_midi = [archivo for archivo in os.listdir(ruta_midi) if archivo.endswith(".mid")]

# Inicializar la barra de progreso
progreso = tqdm(archivos_midi, desc="Procesando archivos MIDI")

# Iterar sobre los archivos MIDI en la carpeta
for archivo_midi in progreso:
    nombre_cancion = os.path.splitext(archivo_midi)[0]  # Obtener el nombre de la canción
    ruta_completa = os.path.join(ruta_midi, archivo_midi)
    
    # Verificar si es un archivo MIDI
    if not os.path.isfile(ruta_completa) or not archivo_midi.lower().endswith('.mid'):
        continue
    
    try:
        # Cargar el archivo MIDI
        mid = mido.MidiFile(ruta_completa)
        
        # Inicializar la lista para la secuencia de esta canción
        secuencia = []
        
        # Procesar el archivo MIDI para convertirlo en secuencias
        for track in mid.tracks:
            for msg in track:
                if msg.type == 'note_on':
                    # Obtener el valor de la nota (0 a 127)
                    nota = msg.note
                    if nota >= 0 and nota <= 47:  # Solo agregar si está en el rango
                        secuencia.append(nota)
        
        # Agregar la secuencia al diccionario
        secuencias_midi[nombre_cancion] = secuencia
    except Exception as e:
        print(f"Error al procesar el archivo {archivo_midi}: {e}")

# Cerrar la barra de progreso
progreso.close()

# Guardar el diccionario en el archivo secuencias_midi.py
with open('secuencias_midi.py', 'w') as archivo:
    archivo.write(f"secuencias_midi = {secuencias_midi}")
