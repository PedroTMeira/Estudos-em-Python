# Planejador de Filmes 3000

## Descrição do Projeto
Sistema de gerenciamento de filmes desenvolvido em Python para controle de uma lista de filmes a assistir. O programa permite adicionar, listar, atualizar e remover filmes, além de manter um histórico de alterações e persistência dos dados em arquivo JSON.

Ideal para organizar sua lista de filmes pendentes, acompanhar o progresso de assistidos e manter um registro das modificações feitas.

## Funcionalidades

- **Adicionar Filmes (ADD):** Cadastra um ou múltiplos filmes de uma só vez na lista.
- **Listar Filmes (LIST):** Exibe todos os filmes salvos, com status de conclusão (assistido ou não) e histórico de alterações.
- **Atualizar Filme (UPDATE):** Permite alterar o nome de um filme e marcar como assistido/não assistido. Registra automaticamente a data da modificação no histórico.
- **Remover Filme (REMOVE):** Exclui um filme da lista permanentemente.
- **Sobre o Criador (ABOUT):** Exibe informações sobre o desenvolvedor.
- **Persistência:** Os dados são automaticamente salvos em um arquivo `portfolio.json` ao sair do programa e carregados na inicialização.

## Conceitos Aplicados

- **Manipulação de arquivos JSON** para persistência de dados (leitura e escrita).
- **Estruturas de dados:** Listas e dicionários para armazenamento e organização dos filmes.
- **Funções modulares:** Cada funcionalidade foi encapsulada em funções específicas (`adicionar_filmes`, `listar_filmes`, `atualizar_filme`, etc.).
- **Tratamento de exceções:** Uso de `try-except` para lidar com erros de entrada do usuário, arquivos não encontrados e JSON inválido.
- **Biblioteca `datetime`:** Para registrar a data e hora das alterações no histórico dos filmes.
- **Interface via terminal:** Menu interativo com validação de entrada do usuário.

## Tecnologias Utilizadas

- **Python 3.x**
- Biblioteca padrão: `json`, `datetime`
