import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from tqdm import tqdm

# Importar los datos de entrenamiento desde secuencias_midi.py
from secuencias_midi import secuencias_midi

# Crear un mapeo de valores de notas originales a valores ajustados en el rango [0, 50)
original_to_adjusted_mapping = {
    original_note_value: adjusted_note_value
    for original_note_value, adjusted_note_value in zip(range(128), range(50))
}

# Obtener las secuencias MIDI
sequences = list(secuencias_midi.values()) # Convertir a lista

# Definir la longitud de las secuencias y el número de notas únicas en los datos
secuencia_longitud = 16
num_notas = 50

# Preprocesar los datos para crear secuencias de entrada y notas objetivo
X = []
y = []

# Limitar el conjunto de datos de entrenamiento inicial
tamano_muestra_inicial = 50
indices_muestra = np.random.choice(len(sequences), size=tamano_muestra_inicial, replace=False)

for idx in indices_muestra:
    seq = sequences[idx]
    for i in range(len(seq) - secuencia_longitud):
        X.append(seq[i:i + secuencia_longitud])
        y.append(seq[i + secuencia_longitud])

# Convertir las listas en arrays NumPy
X = np.array(X)
y = np.array(y)

# Reformatear los datos de entrada para que tengan la forma (batch_size, sequence_length, input_features)
X = X.reshape(-1, secuencia_longitud, 1)

# Dividir los datos en conjuntos de entrenamiento y validación
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de red neuronal
model = keras.Sequential([
    # Capa de entrada
    keras.layers.Input(shape=(secuencia_longitud, 1)),
    # Capas LSTM para aprender secuencias musicales
    keras.layers.LSTM(256, return_sequences=True),
    keras.layers.Dropout(0.2), # Capa de dropout para prevenir sobreajuste
    keras.layers.LSTM(256),
    # Capa completamente conectada para predecir la siguiente nota
    keras.layers.Dense(num_notas, activation='softmax')
])

# Compilar el modelo
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Crear una función para mostrar la barra de progreso
def train_with_progress(model, X_train, y_train, X_val, y_val, epochs=100, batch_size=32):
    progress_bar = tqdm(total=epochs, desc="Training", unit="epoch")
    # Entrenamiento del modelo con seguimiento del progreso
    for epoch in range(epochs):
        # Entrenar el modelo y obtener historial
        history = model.fit(X_train, y_train, batch_size=batch_size, validation_data=(X_val, y_val), verbose=0)
        
        # Actualizar la barra de progreso
        progress_bar.update(1)
        
        # Extraer métricas del historial
        loss = history.history['loss'][0]
        accuracy = history.history['accuracy'][0]
        val_loss = history.history['val_loss'][0]
        val_accuracy = history.history['val_accuracy'][0]
        
        # Mostrar métricas
        progress_bar.set_postfix(loss=loss, accuracy=accuracy, val_loss=val_loss, val_accuracy=val_accuracy)
        
    progress_bar.close()

# Entrena el modelo con seguimiento del progreso
train_with_progress(model, X_train, y_train, X_val, y_val, epochs=50, batch_size=32)

# Guardar el modelo entrenado
model.save('modelo_musical.h5')
