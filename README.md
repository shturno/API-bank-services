# Projeto API Bancária

Este projeto é uma API bancária desenvolvida com Flask. A API permite registrar novos usuários, criar logins e editar saldos de contas bancárias. O projeto também utiliza autenticação JWT para proteger certas rotas.

## Índice

1. [Visão Geral](#visão-geral)
2. [Configuração do Ambiente](#configuração-do-ambiente)
3. [Executando o Projeto](#executando-o-projeto)
4. [Rotas da API](#rotas-da-api)
5. [Author](#author)

## Visão Geral

A API fornece os seguintes recursos:
- **Registro de Usuário**: Permite a criação de um novo usuário.
- **Login**: Permite a criação de uma nova sessão de login.
- **Edição de Saldo**: Permite a atualização do saldo da conta bancária de um usuário, protegido por autenticação JWT.

## Configuração do Ambiente

1. **Clone o Repositório**

   ```bash
   git clone https://github.com/gabrieladsalv/API-bank-login.git
   cd repository

2. **Crie um Ambiente Virtual**

    python -m venv venv

3. **Ative o Ambiente Virtual**

    - Linux/macOS:
        source venv/bin/activate
    - Windows:
        venv\Scripts\activate

4. **Configuração das Variáveis de Ambiente**

    Crie um arquivo .env na raiz do projeto e adicione suas variáveis de configuração. Exemplo:
        SECRET_KEY=your_secret_key
        JWT_SECRET=your_jwt_secret

## Executando o Projeto

    python3 run.py

## Rotas da API

    Registro de Usuário
        Método: POST
        Endpoint: /bank/registry
        Descrição: Registra um novo usuário.
        Request Body: JSON com os detalhes do usuário.
    Login
        Método: POST
        Endpoint: /bank/login
        Descrição: Cria uma nova sessão de login.
        Request Body: JSON com as credenciais do usuário.
    Edição de Saldo
        Método: PATCH
        Endpoint: /bank/balance/<user_id>
        Descrição: Atualiza o saldo da conta bancária do usuário especificado.
        Parâmetros:
            user_id: ID do usuário cuja conta terá o saldo atualizado.
        Request Body: JSON com o novo saldo.
        Autenticação: Requer um token JWT válido no cabeçalho da requisição.

## Author

- name: Gabriela Alvarenga
- contact: gabrielasalvarenga2@gmail.com