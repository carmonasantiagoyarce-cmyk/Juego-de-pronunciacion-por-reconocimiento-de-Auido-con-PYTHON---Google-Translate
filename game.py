# imports
import os
import random
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator
import time

duration = 5
sample_rate = 44100

# Menssages
goodMensajes=[f"!Excelente, lo dijiste bien la palabra era ",f"Ok, Eres muy bueno, mira como lo dijiste "]
badMenssajes=[f"Oh, Lo siento no te entendi, si quieres vuelve a intentarlo","Casi lo logras, Vuelve a intentarlo"]

racha=0
Correctas=0
Incorrectas=0

# Funciones
def GrabarAuidio(Palabra):
    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16")
    sd.wait()
    nombre=f"{Palabra}.wav"
    wav.write(nombre, sample_rate, recording)
    return nombre

def Traducido(nombre):
    recognizer = sr.Recognizer()
    with sr.AudioFile(nombre) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio, language="en")
        translator = Translator()
        translated = translator.translate(text, dest="es")
        return translated.text
    except sr.UnknownValueError:
        print("No se pudo reconocer el habla.")
        return ""   # 🔧 FIX
    except sr.RequestError as e:
        print(f"Error del servicio: {e}")
        return ""   # 🔧 FIX

# Dificultades
easy = [
    ["Hello", "jelou"], ["Dog", "dog"], ["Book", "buk"], ["Cat", "kat"], ["Yes", "yes"],
    ["House", "jaus"], ["Car", "kar"], ["Water", "uóter"], ["Food", "fud"], ["Friend", "frend"]
]

medium= [
    ["Squirrel", "skuírel"], ["Colonel", "kérnel"], ["Schedule", "skedyul"],
    ["Worcestershire", "wustershir"], ["Mischievous", "míschivus"],
    ["Beautiful", "biútiful"], ["Interesting", "íntresting"], ["Different", "dífrent"],
    ["Important", "impórtant"], ["Favorite", "féivorit"]
]

hard = [
    ["Through", "zru"], ["Thought", "zot"], ["Enough", "inóf"], ["Although", "olzóu"],
    ["Knowledge", "nóllech"], ["Strength", "strengz"], ["Develop", "divélop"],
    ["Environment", "enváironment"], ["Government", "góvernmant"], ["Comfortable", "kómfterbol"]
]

# Lecciones
lecciones=0
Actual="easy"
Usados=[]

while lecciones<10:
    time.sleep(1)
    try:
        Dificultad = int(input("Escribe una dificultad facil/1, medio/2, dificil/3: "))
        
        if Dificultad <=3:
            if Dificultad==1:
                Actual="easy"
            elif Dificultad==2:
                Actual="medio"
            elif Dificultad==3:
                Actual="Hard"
            print("El modo escojido es",Actual)
        else:
            continue

        pos=random.randint(0,9)
        datapalabra=""

        if Actual=="easy":
            datapalabra=easy[pos]
        elif Actual=="medio":
            datapalabra=medium[pos]
        elif Actual=="Hard":
            datapalabra=hard[pos]

        print(datapalabra)

        if datapalabra:
            palabra=datapalabra[0]
            pronuciacion=datapalabra[1]
            print(f" La palabra es {palabra}, para que te valla bien, aqui esta su pronunciacion: {pronuciacion}")

        time.sleep(1)
        print("Pronuncia ahora, que se escuhce 🤑😎🔊🔊")

        archivo=GrabarAuidio(palabra)
        traducion=Traducido(archivo)

        # 🔧 FIX aquí
        if traducion:
            lowered=traducion.lower()
        else:
            lowered=""

        pos=random.randint(0,1)
        frase=""

        if lowered==palabra.lower():
            frase=f"{goodMensajes[pos]}{palabra}"
            racha+=1
            Correctas+=1
        else:
            Incorrectas+=1
            if racha > 0:
                print("💥 ¡Perdiste tu racha! 😱 Pero tranquilo... ¡puedes recuperarla! 🔥💪")
            racha=0
            frase=badMenssajes[pos]

        print(frase)

        if racha >=5:
            print(f"🚀 ¡Vamos! ¡Mantén esa racha de {racha} viva, tú puedes! 🔥😎")
        else:
            print(f"Mira tu racha {racha}")
    except ValueError:
        print("Escribe el numero al que pertenece tu dificultad")
    lecciones += 1

print(f"🔥 Racha final: {racha}")
print(f"🎯 Respuestas correctas: {Correctas}")
print(f"💀 Respuestas incorrectas: {Incorrectas}")