import wave
import numpy as np

#Convierte el audio good morning de bytes a enteros

#ondaconvertida = np.frombuffer(signal_gm, dtype='int16')

#cargar archivo wav en la variable

goodmorning = wave.open('good-morningMan.wav', 'r')

frames = goodmorning.readframes(-1)

#obtener todos los frames del onjeto wave
ondaconvertida = np.frombuffer(frames, dtype='int16')

#mostrar el resultado de frames
print (ondaconvertida[:10])
   
