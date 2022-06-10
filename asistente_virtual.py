import speech_recognition as speech
import pyttsx3
import random as rm
import datetime as time
import requests as req
import pywhatkit as tk
import webbrowser

# Permite reconocer la voz
listener = speech.Recognizer()

engine = pyttsx3.init()

#RATE DEL ASISTENTE
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)

#VOZ DEL ASISTENTE
voice_engine = engine.getProperty('voices')
print("Voces: " + str(voice_engine))
engine.setProperty('voice', voice_engine[0].id)

meses = {
    'January': 'Enero',
    'February': 'Febrero',
    'March': 'Marzo',
    'April': 'Abril',
    'May': 'Mayo',
    'June': 'Junio',
    'July': 'Julio',
    'August': 'Agosto',
    'September': 'Septiembre',
    'October': 'Octubre',
    'November': 'Noviembre',
    'December': 'Diciembre'
}

name="PJEM"
url = "http://localhost/electronico/buscar/persona.php"

def saludo():
    hour = int(time.datetime.now().hour)
    if hour>= 0 and hour<12:
        talk("Buenos dias !")
  
    elif hour>= 12 and hour<18:
        talk("Buenas tardes !")   
  
    else:
        talk("Buenas noches !")  
  
    talk(random_saludo())
    
#SALUDO ALEATORIO DE BIENVENIDA DEL ASISTENTE
def random_saludo():
    lista = ['como puedo ayudarte','dime, que puedo hacer por ti','en que te puedo ayudar']
    seleccion = rm.choice(lista)
    return seleccion

#CONVIERTE EL TEXTO A VOZ POR EL ASISTENTE
def talk(text):
    engine.say(text)
    engine.runAndWait()

#ENVIA WHATSAPP
def whatsapp_enviar(numero,mensaje):  
    try:
        tk.sendwhatmsg(numero,mensaje,  22, 28) 
        print("Envio Exitoso!")  
    except:
        print("Ha ocurrido un error!") 

#BUSCA VIDEOS DE YOUTUBE
def reproduce(texto):  
    try:
        tk.playonyt(texto) 
        print("Viendo video!")  
    except:
        print("Ha ocurrido un error!") 
#BUSCAR PERSONAS EN SISTEMA
def buscar_persona(nombre):
    print("Nombre a buscar: " + nombre)
    result = req.get(url,params={"nombre":nombre})
    if result.status_code == 200:
        print("Resultados: " + result.text)
    elif result.status_code==404:
        print("no se encontrol la pagina")
        print("Resultados: " + result.text) 
#ACTIVA MICROFONO PARA ATENDER SOLICITUD
def escuchar():
    try:
        with speech.Microphone() as source:
            voice = listener.listen(source)
            recognizer = listener.recognize_google(voice, language='es-MX',show_all=False)
            print("Texto: " + str(recognizer))
            recognizer = recognizer.lower()

            if name in recognizer:
                recognizer = recognizer.replace(name, '')
            print(recognizer)

        return  recognizer  
    except (RuntimeError, TypeError, NameError):
        print('Algo ha salido mal ' + str(NameError))
        pass

def run():

    saludo()
    recognizer = escuchar()
    print("Texto Capturado: " + str(recognizer) )   

    # IDENTIFICA EL MES
    if 'mes' in recognizer:
        mes = time.datetime.now().strftime('%B')
        mes_translate = meses[mes]
        talk('Estamos en el mes de ' + str(mes_translate))
        talk("Deseas algo mas") 
    elif 'buscar' in recognizer: 
        talk("¿que deseas buscar?")
        subrecognizer = escuchar()
        # IDENTIFICA EL MES
        if 'persona' in subrecognizer:
            talk("¿cual es nombre a buscar?")
            persona = escuchar()
            buscar_persona(persona)
            talk("Deseas algo mas") 
    elif 'whatsapp' in recognizer:
        talk("¿cual es el numero al que se enviara el whatsapp?")
        numero = escuchar()   
        talk("¿cual es el mensaje?")
        msg = escuchar()   
        whatsapp_enviar(numero,msg) 
        talk("Deseas algo mas")   
    elif 'reproducir' in recognizer:
        talk("¿que deseas ver en youtube?")
        video = escuchar()   
        reproduce(video)   
        talk("Deseas algo mas") 
    elif 'electrónico' in recognizer:
        webbrowser.open("https://electronico.pjedomex.gob.mx", new=2, autoraise=True)
        talk("Deseas algo mas")  
    elif 'sigejupe' in recognizer:
        webbrowser.open("https://sigejupe2.pjedomex.gob.mx", new=2, autoraise=True)
        talk("Deseas algo mas")     
    elif 'sigejupe' in recognizer:
        webbrowser.open("https://www.pjedomex.gob.mx", new=2, autoraise=True)
        talk("Deseas algo mas")            
    else: 
        talk('Disculpa, no te entiendo, debes hablar mas claro')     