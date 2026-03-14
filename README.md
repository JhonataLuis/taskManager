# 🗂️ Task Manager - Gerenciador de Tarefas

![Python](https://img.shields.io/badge/python-≥3.10-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.x-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple)
![License](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Versão](https://img.shields.io/badge/versão-1.0-blue)

---

## 📌 Descrição
O **Task Manager** é uma aplicação web simples e intuitiva para gerenciamento de tarefas diárias, desenvolvida com **Python**, **Django** e **Bootstrap**.  

O sistema permite que usuários organizem suas atividades de forma eficiente através de um **CRUD completo de tarefas**.

---

## 📖 Detalhes
Este projeto foi desenvolvido com o objetivo de **praticar conceitos de desenvolvimento web fullstack**, como:  
- Integração entre **frontend e backend**  
- Persistência de dados com **ORM e PostgreSQL**  
- Templates dinâmicos com **Django**  

É ideal para **equipes que desejam centralizar suas tarefas em um ambiente simples e eficiente**. 

## ✨ Funcionalidades

### ✅ CRUD Completo

**Create**  
Adicionar novas tarefas com título, descrição, datas e prioridade.

**Read**  
Visualizar a lista de todas as tarefas cadastradas.

**Update**  
Editar informações de tarefas existentes.

**Delete**  
Remover tarefas concluídas ou indesejadas.

---

## 🚀 Tecnologias Utilizadas

**Backend**
- Python
- Django

**Frontend**
- HTML5
- Bootstrap 5

**Banco de Dados**
- PostgreSQL (Desenvolvimento)

**Outros**
- Bootstrap Icons
- Git
- GitHub

---

## 📌 Campos da Tarefa

| Camada         | Tecnologias /Ferramentas                |
|----------------|----------------------------|
| Backend        | Python, Django             |
| Frontend       | HTML5, CSS3, Javascript    | 
| UI / Estilo    | Bootstrap                  | 
| Banco de Dados | PostgreSQL                 |

---

## 📁 Estrutura do Projeto

taskManager/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── .gitignore
├── core/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py # Modelo Task
│ ├── views.py # Funções salvar, lista, editar, deletar
│ ├── urls.py # Rotas da aplicação
│ ├── migrations/
│ └── templates/
│ ├── index.html
│ └── update.html
└── config/
├── init.py
├── settings.py
├── urls.py
└── wsgi.py


---

# 🖥️ Como Executar o Projeto

## Pré-requisitos

- Python 3.8+
- Git
- PostgreSQL (opcional)

---

## ⚙️ Instalação e Execução

```bash
# 1. Clone o repositório
git clone https://github.com/JhonataLuis/taskManager.git

# 2. Entre na pasta do projeto
cd taskManager

# 3. Crie um ambiente virtual
python -m venv venv

# 4. Ative o ambiente virtual

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate

# 5. Instale as dependências
pip install -r requirements.txt

# 6. Execute as migrações
python manage.py migrate

# 7. Inicie o servidor
python manage.py runserver

# 8. Acesse no navegador
👉 http://127.0.0.1:8000

🔄 Rotas da Aplicação

| URL                  | Método     | Função  | Descrição              |
| -------------------- | ---------- | ------- | ---------------------- |
| `/`                  | GET        | lista   | Lista todas as tarefas |
| `/salvar/`           | POST       | salvar  | Cria nova tarefa       |
| `/editar/<int:id>/`  | GET / POST | editar  | Edita tarefa           |
| `/deletar/<int:id>/` | GET        | deletar | Remove tarefa          |

🔑 Funcionalidades

✅ Lista de Tarefas

Visualização em tabela com todas as tarefas e seus status.

✅ Criação de Tarefa

Formulário simples para cadastro de novas tarefas.

✅ Edição

Formulário preenchido automaticamente para atualização de dados.

✅ Exclusão

Remoção com confirmação para evitar exclusões acidentais.

🤝 Contribuições

Contribuições são sempre bem-vindas!

Faça um fork do projeto

Crie uma branch para sua feature

git checkout -b feature/nova-feature

Commit suas mudanças

git commit -m "Adiciona nova feature"

Envie para sua branch

git push origin feature/nova-feature

Abra um Pull Request

👨‍💻 Autor

Jhonata Luis

💼 LinkedIn: https://www.linkedin.com/in/jhonataluisdesenvolvedorjava/

🐙 GitHub: https://github.com/JhonataLuis
