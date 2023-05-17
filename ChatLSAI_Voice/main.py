import os
import openai
from fala import ler_resposta
from reconhecimentoJarvis import iniciar_reconhecimento

# Chave de API do OpenAI
API_KEY = os.getenv('GPT_APP_KEY')

# Configurar a API do OpenAI com a chave de API
openai.api_key = API_KEY

def main():
    # Mensagem inicial fixa no topo da tela
    mensagem_inicial = """
    Bem-vindo ao ChatLSAI!
    
    Você pode conversar com o Assistente digitando suas perguntas.
    O Assistente irá responder de acordo com a sua entrada.
    Digite 'sair' a qualquer momento para encerrar o programa.
    
    Para fazer uma pergunta por voz, diga 'Jarvis' e aguarde as instruções.
    """
    os.system('clear' if os.name == 'posix' else 'cls')

    contexto = "Somos velhos amigos numa conversa informal, pode falar usando gírias"
    print(mensagem_inicial)

    while True:

        #pergunta = input("Você: ")
        pergunta = iniciar_reconhecimento()
        
        if pergunta.lower() == "sair":
            print("Encerrando o programa...")
            break

        resposta = obter_resposta(contexto, pergunta)
        print("Assistente:", resposta)
        ler_resposta(resposta)

def obter_resposta(contexto, pergunta):
    try:
        # Combinar o contexto e a pergunta em um único prompt
        prompt = f"{contexto}\nVocê: {pergunta}\nAssistente:"

        # Fazer uma solicitação para a API do GPT-3 para obter a resposta
        resposta = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=250,
            n=1,
            stop=None,
            temperature=0.7
        )

        return resposta.choices[0].text.strip()
    except Exception as e:
        print("Ocorreu um erro na comunicação com o ChatLSAI. Por favor, tente novamente.")
        print(f"Detalhes do erro: {str(e)}")
        return ""

if __name__ == "__main__":
    main()
