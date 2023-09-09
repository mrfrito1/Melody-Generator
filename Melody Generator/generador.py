import numpy as np
import random
from scales import scale
import mido
from mido import MidiFile, MidiTrack, Message, MetaMessage
from tensorflow import keras
from rhythms import rhythms

# Define la longitud de las secuencias y el número de notas únicas en los datos
secuencia_longitud = 16
num_notas = 12  # Cambiado a 12 para representar una octava

# Cargar el modelo entrenado
model = keras.models.load_model('modelo_musical.h5')

# Variables para la selección de escala y nota raíz
selected_scale = 'Major'
root_note_name = 'c'

# Define los tiempos de las notas posibles (en ticks de MIDI)
durations = [960, 480, 240, 120, 60, 30]

# Seleccionar la escala
from scales import scale  # Asumiendo que la función está en un archivo scales.py en el mismo directorio

selected_scale = scale[selected_scale]  # Obtener la lista de tonos de la escala seleccionada

def generar_melodia(model, longitud_melodia, semilla):
    melodia_generada = list(semilla)
    for _ in range(longitud_melodia):
        if len(melodia_generada) < secuencia_longitud:
            entrada = np.array(melodia_generada).reshape(1, len(melodia_generada), 1)
        else:
            entrada = np.array(melodia_generada[-secuencia_longitud:]).reshape(1, secuencia_longitud, 1)
        prediccion = model.predict(entrada)
        # Obtener las probabilidades y normalizarlas
        probabilidades = prediccion.ravel()
        
        # Aplicar la escala seleccionada
        probabilidades_escala = [probabilidades[i] if i % num_notas in selected_scale else 0 for i in range(len(probabilidades))]
        
        # Introducir aleatoriedad: Muestrear de las probabilidades en lugar de tomar la máxima
        siguiente_nota = np.random.choice(len(probabilidades_escala), p=probabilidades_escala/sum(probabilidades_escala))
        melodia_generada.append(siguiente_nota)
    
    # Agregar patrones rítmicos
    melodia_final = []
    for nota in melodia_generada:
        if nota != -1:
            nota = (nota + 24) % num_notas  # Asegurarse de que la nota esté en el rango de C1
        duracion = random.choice(durations) if nota != -1 else random.choice(durations)
        melodia_final.append((nota, duracion))
    
    return melodia_final

# Función para guardar la melodía en un archivo MIDI
def guardar_melodia_midi(melodia, nombre_archivo):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    tiempo = 0 # Mantén un seguimiento del tiempo
    for nota, duracion in melodia:
        if nota != -1:
            nota = (nota + 60) % 128  # Asegurarse de que la nota esté en el rango de C1
        # Elije una duración aleatoria
        track.append(Message('note_on', note=nota, velocity=64, time=0))
        track.append(Message('note_off', note=nota, velocity=64, time=duracion))
        tiempo += duracion
    # Añade un evento de finalización
    track.append(MetaMessage('end_of_track'))
    mid.save(nombre_archivo)

# Semilla inicial para la melodía (limitada a una octava)
semilla_inicial = [60, 62, 64, 65, 67, 69]

# Asegurarse de que la semilla inicial tenga la longitud adecuada
while len(semilla_inicial) < secuencia_longitud:
    nota_aleatoria = random.randint(0, num_notas - 1)
    semilla_inicial.append(nota_aleatoria)

# Generar melodía MIDI basada en el modelo
longitud_melodia_generada = 100
melodia_generada = generar_melodia(model, longitud_melodia_generada, semilla_inicial)

# Guardar la melodía generada en un archivo MIDI
nombre_archivo_midi = "melodia_generada.mid"
guardar_melodia_midi(melodia_generada, nombre_archivo_midi)
