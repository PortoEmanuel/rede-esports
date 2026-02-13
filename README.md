# 🎮 Rede Esports v2

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

A **Rede Esports** é uma plataforma robusta projetada para gerenciar ecossistemas de esportes eletrônicos. O sistema separa de forma inteligente o ambiente de **Redação/Trabalho** do portal da **Comunidade**, permitindo uma gestão editorial profissional e um engajamento profundo com os torcedores.

## 🚀 Funcionalidades Principais

- **Custom User Model**: Sistema de autenticação personalizado separando Membros de Equipe.
- **Ecossistema de Equipe**: Gestão dinâmica de cargos (Designers, Escritores, Fotógrafos).
- **Portal da Comunidade**: Perfis automáticos para membros com foco em captura de Leads e Gamificação.
- **Automação com Signals**: Criação automática de perfis de usuário via gatilhos do Django.
- **Admin Customizado**: Painel administrativo totalmente em PT-BR e organizado por domínios.

## 🛠️ Tecnologias
- **Framework:** Django 5.2.11
- **Linguagem:** Python 3.11+
- **Banco de Dados:** SQLite (Desenvolvimento)


## 🆕 Novidades da Versão (Sprint Atual)

- **Dashboard do Redator:** Ambiente logado exclusivo para criação e edição de conteúdos fora do painel administrativo.
- **Editor Rich Text (Summernote):** Interface de escrita profissional com suporte a formatação, imagens e links diretamente no front-end.
- **Métricas de Engajamento:** Contador de visualizações por notícia e listagem de matérias por autor.
- **Fluxo de Autenticação Customizado:** Páginas de Login/Logout personalizadas para a equipe.

## ⚙️ Como executar

1. Clone o repositório: `git clone https://github.com/seu-usuario/rede-esports.git`
2. Ative seu ambiente virtual: `source .venv/bin/activate` (Linux) ou `.venv\Scripts\activate` (Windows)
3. Instale as dependências: `pip install -r requirements.txt`
4. Aplique as migrações: `python manage.py migrate`
5. Inicie o servidor: `python manage.py runserver`