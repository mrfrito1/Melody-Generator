import mido
from mido import MidiFile, MidiTrack, Message, MetaMessage
import numpy as np
import random
import os
from scales import scale  # Importa la escala desde tu archivo scales.py

# Variables globales
selected_scale = "Major"  # Escala predeterminada
root_note_name = "g"  # Nota raíz predeterminada

# Función para generar una nota aleatoria de la escala
def random_note_from_scale(root_note, scale_name):
    scale_intervals = scale[scale_name]
    random_interval = random.choice(scale_intervals)
    root_index = note_names.index(root_note)
    note_index = (root_index + random_interval) % len(note_names)
    return note_index

# Función para generar una melodía y guardarla en un archivo MIDI
def generate_melody_to_file(file_path):
    if file_path:
        midi_file = MidiFile()
        track = MidiTrack()
        midi_file.tracks.append(track)
        track.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))

        for _ in range(melody_length):
            note_index = random_note_from_scale(root_note_name, selected_scale)
            if note_index < 0 or note_index >= len(note_names):
                continue
            note_value = note_to_midi[note_names[note_index]]
            track.append(Message('note_on', note=note_value, velocity=64, time=0))
            track.append(Message('note_off', note=note_value, velocity=64, time=note_duration))

        midi_file.save(file_path)
        print(f"Archivo MIDI generado en:\n{file_path}")
    else:
        print("La variable file_path no está definida correctamente.")

# Definir la escala seleccionada
selected_scale = 'Major'

# Parámetros de generación de melodía
melody_length = 16
note_duration = 480
tempo = 120

note_to_midi = {
    'c': 60, 'c#': 61, 'd': 62, 'd#': 63, 'e': 64, 'f': 65,
    'f#': 66, 'g': 67, 'g#': 68, 'a': 69, 'a#': 70, 'b': 71
}

# Definir nombres de nota
note_names = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"]

# Variables para la selección de escala y nota raíz
scale_var = "Major"
note_var = "c"

