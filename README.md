Generador de Melodías MIDI en Python.

Este repositorio contiene una aplicación en Python que genera melodías MIDI. Puedes seleccionar la escala y la nota raíz para personalizar tus composiciones. La aplicación incluye una interfaz gráfica simple para facilitar la interacción.

Uso
Asegúrate de tener Python instalado en tu sistema.

Clona este repositorio o descárgalo como archivo ZIP y descomprímelo en tu computadora.

Abre una terminal en la ubicación del repositorio.

Ejecuta la aplicación utilizando el siguiente comando:

python app.py

La interfaz gráfica se abrirá y te permitirá cambiar la escala y la nota raíz. Además, puedes generar una melodía haciendo clic en el botón "Generar Melodía".

Estructura del Repositorio
app.py: El punto de entrada de la aplicación que inicia la interfaz gráfica y controla la interacción del usuario.

scales.py: Contiene definiciones de escalas musicales en forma de diccionario.

gui.py: Maneja la interfaz gráfica utilizando la biblioteca Pygame. Permite al usuario cambiar la escala y la nota raíz.

main.py: Genera melodías MIDI basadas en la escala y la nota raíz seleccionadas.

Escalas Musicales
Puedes personalizar tu composición seleccionando una escala musical. Las escalas disponibles son:

Major (Mayor)
Minor (Menor)
Notas Musicales
Selecciona la nota raíz para tu melodía. Las notas disponibles son:

C, C#, D, D#, E, F, F#, G, G#, A, A#, B
Generación de Melodías
La aplicación genera una melodía MIDI con las siguientes características:

Longitud de la melodía: 16 notas
Duración de las notas: 480 milisegundos
Tempo: 120 BPM
Guardar Melodías
La melodía generada se guardará automáticamente como un archivo MIDI en el escritorio de tu usuario. Puedes encontrar el archivo en la ubicación ~/Desktop/melodia.mid.

¡Diviértete experimentando con diferentes escalas y notas para crear tus propias composiciones musicales!
