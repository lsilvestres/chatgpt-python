import time
import speech_recognition as sr

def listen_for_activation():
    r = sr.Recognizer()

    # Definir o idioma para português do Brasil (opcional)
    r.energy_threshold = 4000  # Ajustar o limiar de energia conforme necessário

    # Definir o tempo máximo de espera para uma frase (em segundos)
    r.phrase_time_limit = 0.5

    with sr.Microphone() as source:
        print("Aguardando ativação...")

        while True:
            audio = r.listen(source)

            try:
                speech = r.recognize_google(audio, language="pt-BR")
                print("Você disse:", speech)
                if "jarvis" in speech.lower():
                    print("Ativação detectada!")
                    # Obter o texto depois da palavra "jarvis"
                    text = speech.lower().split("jarvis", 1)[1].strip()
                    print("Texto:", text, "\n")
                    #return text

            except sr.UnknownValueError:
                print("Não foi possível reconhecer o áudio.")
            except sr.RequestError as e:
                print("Erro ao fazer a solicitação ao serviço de reconhecimento de fala:", str(e))

            # Reduzir o tempo de espera para 1 segundo
            #time.sleep(1)

def main():
    text = listen_for_activation()

    # Restante do código...

if __name__ == "__main__":
    main()
