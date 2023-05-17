import time
import speech_recognition as sr

def iniciar_reconhecimento():
    r = sr.Recognizer()

    # Definir o idioma para português do Brasil (opcional)
    r.energy_threshold = 4000  # Ajustar o limiar de energia conforme necessário

    # Definir o tempo máximo de espera para uma frase (em segundos)
    r.phrase_time_limit = 0.5

    with sr.Microphone() as source:
        while True:
            audio = r.listen(source)
            
            try:
                speech = r.recognize_google(audio, language="pt-BR")
                print("Você disse:", speech)
                if "bia" in speech.lower():
                    # Obter o texto depois da palavra "jarvis"
                    text = speech.lower().split("bia", 1)[1].strip()
                    return text
                    #return text                
            
            except sr.UnknownValueError:
                print("")

            except sr.RequestError as e:
                print("Erro ao fazer a solicitação ao serviço de reconhecimento de fala:", str(e))
                return ""

            # Reduzir o tempo de espera para 1 segundo
            #time.sleep(1)