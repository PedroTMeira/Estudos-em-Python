import datetime
import json

arquivo_dados = "portfolio.json"

def carregar():
    try:
        with open(arquivo_dados, "r", encoding="utf-8") as arquivo:
            dados_carregados = json.load(arquivo)
            return dados_carregados
    except FileNotFoundError:
        print(f"Não consegui ler {arquivo_dados}. Pode ser que tenha algum erro aí, vou começar com uma lista vazia.")
        return []
    except json.JSONDecodeError:
        print(f"Não consegui ler {arquivo_dados}. Pode ser que tenha algum erro aí, vou começar com uma lista vazia.")
        return []

def salvar():
    try:
        with open(arquivo_dados, "w", encoding="utf-8") as arquivo:
            json.dump(projetos, arquivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")

def buscar_projeto(nome_projeto):
    for projeto in projetos:
        if projeto['nome'] == nome_projeto:
            return projeto
    return None

def adicionar_filmes():
    try:
        cadastros = int(input("Digite o número de filmes que gostaria de adicionar: " "\n Sua resposta: "))
        if cadastros >= 1:
            for i in range(cadastros):
                projeto = input(f"Digite o nome do {i + 1}° filme: " "\n Sua resposta: ")
                if projeto:
                    filmes_cadastrados = {
                        "nome": projeto,
                        "concluido": False,
                        "historico": []
                    }
                    projetos.append(filmes_cadastrados)
                    print(f"O filme {projeto} foi adicionado!")
        else:
            print("Precisa ser um número válido, tente novamente")

    except ValueError:
        print("Não entendi esse número, tente novamente")

def listar_filmes():
    if len(projetos) == 0:
        print("Você não tem filmes salvos ainda :( que tal adicionar um hoje ?")
    else:
        print("Você possui estes filmes te esperando!")
        print("Segue a lista:")
        contador = 1
        for projeto in projetos:
            print()
            print(f"{contador}° Filme: {projeto['nome']}")
            print(f"   Assistido ?: {'Sim' if projeto['concluido'] else 'Ainda não'}")
            print(f"   Histórico: {projeto['historico']}")
            contador += 1

def atualizar_filme():
    atualizar = input("Qual filme você deseja alterar ? " "\n Sua resposta: ")
    atualizado = buscar_projeto(atualizar)

    if atualizado is None:
        print("Filme não encontrado, tente novamente!")
        return

    atualizado["nome"] = input("Tudo bem, vamos la! Qual será o novo filme ? " "\n Sua resposta: ")
    atualizado["concluido"] = bool(input("Já assistiu esse filme ? (1 para sim e 0 para não)" "\n Sua resposta: "))

    data = datetime.date.today()
    modificado = (data, atualizado["nome"], atualizado["concluido"])
    atualizado["historico"].append(modificado)
    print("Filme atualizado com sucesso!")

def remover_filme():
    excluir = input("Qual filme você deseja excluir ? " "\n Sua resposta: ")
    excluido = buscar_projeto(excluir)

    if excluido is not None:
        projetos.remove(excluido)
        print(f"Poxa, o filme {excluido['nome']} foi removido, que pena!")
    else:
        print("Filme não encontrado, tente novamente!")

def sobre_aplicativo():
    print("\n" + "~" * 50)
    print("Programa criado por Pedro.")
    print("Possui o intuito de organizar filmes :)")
    print("~" * 50)

print("Carregando dados salvos...")
projetos = carregar()
print(f"{len(projetos)} filmes carregados com sucesso!")

while True:
    print("\n" + "="*50)
    print("Planejador de filmes 3000!")
    print("="*50)
    print("Comandos: ")
    print("ADD - Adicionar um filme.")
    print("LIST - Ver sua lista de filmes.")
    print("UPDATE - Atualizar um filme que já esta salvo")
    print("REMOVE - Exclua um filme que foi salvo")
    print("ABOUT - Sobre o criador.")
    print("QUIT - Sair do programa.")
    print("-"*50)
    ordem = input("O que deseja fazer hoje ?" "\n Sua resposta: ").upper()

    if ordem == 'ABOUT':
        sobre_aplicativo()
    elif ordem == 'QUIT':
        try:
            print("Salvando seus dados...")
            salvar()
            print("Dados salvos com sucesso!")
        except Exception as e:
            print(f"ERRO ao salvar dados: {e}")
        print("Obrigado por utilizar o programa!")
        break
    elif ordem == "ADD":
        adicionar_filmes()
    elif ordem == "LIST":
        listar_filmes()
    elif ordem == "UPDATE":
        atualizar_filme()
    elif ordem == "REMOVE":
        remover_filme()

    else:
        print("Ainda não temos este comando :( tente novamente!")

print("Nos vemos em breve!")