import os
import openai
import time

# Chave de API do OpenAI
API_KEY = 'YOUR APP KEY'

# Configurar a API do OpenAI com a chave de API
openai.api_key = API_KEY

def obter_resposta(contexto, pergunta):
    
    success = False
    resposta = ""

    while(success == False):
        try:
            # Combinar o contexto e a pergunta em um único prompt
            prompt = f"{contexto}\nVocê: {pergunta}\nAssistente:"

            openai.api_key = API_KEY

            # Fazer uma solicitação para a API do GPT-3 para obter a resposta
            resposta = openai.Completion.create(
                engine='text-davinci-003',
                prompt=prompt,
                max_tokens=2000,
                n=1,
                stop=None,
                temperature=0.7
            )
            

            #print(resposta)
            resposta = resposta.choices[0].text.strip()
            success = True
        except Exception as e:
            print("\033[91mOcorreu um erro na comunicação com o ChatLSAI. Por favor, tente novamente.\033[0m")
            print(e)
            print(contexto)
            openai.api_key = ""
            time.sleep(1)
            openai.api_key = API_KEY
            success = False
            

    return resposta
    
    

def exibir_mensagem_inicial():
    mensagem_inicial = [
        "Bem-vindo ao ChatLSAI!",
        "",
        "Você pode conversar com o Assistente digitando suas perguntas.",
        "O Assistente irá responder de acordo com a sua entrada.",
        "Digite 'sair' a qualquer momento para encerrar o programa.",
        "",
        "Aguarde enquanto o modelo LSAI está sendo inicializado..."
    ]
    os.system('clear' if os.name == 'posix' else 'cls')
    print("\n".join(mensagem_inicial))

def main():
    exibir_mensagem_inicial()
    contexto = """
        Você só pode responder perguntas relacionadas ao texto abaixo
        Seu nome é Bia, você é filha do mestre Yoda do star wars. Você deve falar como o mestre Yoda. Pode contar pra todo mundo quem é o seu pai
        Sua função é ajudar o usuário na utilização de serviços da área de SRE, como orientar na abertura de chamados ou passar informações pertinentes a infraestrutura e ambientes

        "Tipo de chamados
            Troubleshooting
                Descrição: Identificação de problemas recorrentes que não estão impactando significamente o ambiente
                link: "http://awx.dock.tech/troubleshooting/"
            GMud
                Descrição: Mudanças que devem ser realizadas em infraestrutura e ambientes cloud
                link: "http://awx.dock.tech/change/"
            Incidente
                Descrição: Resolução de problemas urgentes que estejam impactando os ambientes e consequentemente usuários e clientes
                link: "http://awx.dock.tech/incidente/"
            Análise de performance
                Descrição: Avaliar performance de aplicações, TMR, througpout, latência, saturação, taxa de erros e etc. Problemas que afetam o ambiente mas não estão gerando indiponibilidade ou alto impacto para os usuários
                link: "http://awx.dock.tech/anal_per/"
            Planejamento de capacidade
                Descrição: Avaliação da capacidade da aplicação e infraestrutura a longo prazo
                link: "http://awx.dock.tech/cap_plan/"
            Migração de ambiente"
                Descrição: Migrar infraestrutura de lugar, entre clouds ou datacenters
                link: "http://awx.dock.tech/migr_env/"

        Caso a resposta não esteja no texto, diga que não possuí essa resposta
        Caso a resposta deixe duas opções muito próximas, faça perguntas ao usuário para saber qual opções é mais adequada
        Sempre faça pelo menos mais uma pergunta para garantir que vai dar a resposta correta. Peças mais informações sobre o comportamento do problema relatado
        Sempre que sugerir um tipo de chamado, adicione ao final do texto duas linhas em branco e o tipo de chamado com o caracter # antes e depois
        Só use # antes e depois do tipo de chamado, quando tiver a sugestão definitiva com apenas um tipo de chamado
    """
    
    pergunta = ""

    while True:
        #os.system('clear' if os.name == 'posix' else 'cls')
        #exibir_mensagem_inicial()

        pergunta = input("\033[94mVocê: \033[0m")
        if pergunta.lower() == "sair":
            break

        resposta = obter_resposta(contexto, pergunta)
        if resposta:
            print("\n\033[93mAssistente:\n", end="")
            #print(resposta)
            resposta = resposta.replace('\n', ' ')

            for char in resposta:
                print(char, end="", flush=True)
                if char == "," or char == ".":
                    time.sleep(0.3)  # Pausa para pontuação
                elif char == " ":
                    time.sleep(0.1)  # Pausa para espaços
                else:
                    time.sleep(0.04)  # Pausa para outras letras e caracteres
            print("\033[0m")            
            print("\n")



        contexto += f"\nVocê: {pergunta}\nAssistente: {resposta}"

        time.sleep(1)

if __name__ == '__main__':
    main()
