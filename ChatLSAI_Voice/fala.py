from playsound import playsound
from gtts import gTTS

def ler_resposta(resposta):
    tts = gTTS(resposta, lang='pt-br')
    tts.save('resposta.mp3')
    playsound('resposta.mp3')

