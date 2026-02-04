# 🍽️ Daily Diet

## 📝 Sobre o projeto

API REST completa para gerenciamento de dieta diária desenvolvida com **Flask**, **Flask-Login** e **MySQL** containerizado com **Docker**. O projeto implementa um sistema de autenticação robusto e CRUD completo para registro e acompanhamento de refeições, permitindo que usuários monitorem sua alimentação e verifiquem se estão seguindo a dieta.

Ideal para aprendizado de:
- Sistema de autenticação com Flask-Login
- Relacionamentos entre tabelas (User-Meals)
- CRUD completo com rotas protegidas
- Criptografia de senhas com bcrypt
- Containerização com Docker
- ORM com SQLAlchemy
- Validação de permissões por usuário

## 🚀 Tecnologias utilizadas

- **Python 3.x**
- **Flask 2.3.0** - Framework web
- **Flask-SQLAlchemy 3.1.1** - ORM para banco de dados
- **Flask-Login 0.6.2** - Gerenciamento de autenticação e sessões
- **bcrypt** - Criptografia de senhas
- **MySQL** - Banco de dados relacional
- **Docker** - Containerização do banco de dados
- **PyMySQL 1.1.0** - Conector MySQL para Python
- **Werkzeug 2.3.0** - WSGI toolkit
- **Cryptography 41.0.7** - Biblioteca de criptografia
- **Requests 2.31.0** - HTTP library

## ⚙️ Como executar

### Pré-requisitos

- Python 3.x instalado
- Docker e Docker Compose instalados
- pip (gerenciador de pacotes Python)

### Configuração do Banco de Dados com Docker

1. Inicie o container MySQL usando Docker Compose:
```bash
docker-compose up -d
```

2. Verifique se o container está rodando:
```bash
docker ps
```

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/luisaferreirass/Daily-Diet.git
cd Daily-Diet
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
```

3. Ative o ambiente virtual:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Executando a aplicação
```bash
python app.py
```

A API estará disponível em: `http://localhost:5000`

### Parando os serviços
```bash
# Parar o container MySQL
docker-compose down

# Parar e remover volumes (apaga os dados)
docker-compose down -v
```

## 🐳 Configuração do Docker

### Credenciais do MySQL (docker-compose.yml)
```yaml
MYSQL_USER: admin
MYSQL_PASSWORD: admin123
MYSQL_DATABASE: daily-diet
MYSQL_ROOT_PASSWORD: admin123
Port: 3307:3306
```

### Conexão da aplicação
```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin123@127.0.0.1:3307/daily-diet'
```

## 🎯 Funcionalidades

### Gerenciamento de Usuários
- 📝 **Criar** conta de usuário
- 🔑 **Login** com autenticação segura
- 🚪 **Logout** para encerrar sessão
- 👤 **Visualizar** perfil do usuário
- ✏️ **Atualizar** senha do usuário
- 🗑️ **Deletar** conta de usuário

### Gerenciamento de Refeições
- ➕ **Adicionar** refeições diárias
- 📋 **Listar** todas as refeições do usuário
- 🔍 **Visualizar** detalhes de uma refeição específica
- ✏️ **Editar** informações de refeições
- 🗑️ **Deletar** refeições
- ✅ **Marcar** se está dentro da dieta ou não

## 🛠️ Modelos de dados

### User (Usuário)

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | Integer | Chave primária (auto-incremento) |
| username | String | Nome de usuário (único) |
| password | String | Senha criptografada com bcrypt |

### Meal (Refeição)

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | Integer | Chave primária (auto-incremento) |
| name | String | Nome da refeição |
| description | String | Descrição da refeição |
| date | String | Data da refeição |
| hour | String | Horário da refeição |
| inTheDiet | Boolean | Está dentro da dieta? |
| id_user | Integer | Chave estrangeira (User) |

**Relacionamento:** Um usuário pode ter várias refeições (1:N)

## 📸 Endpoints da API

### Autenticação

| Método | Endpoint | Descrição | Autenticação |
|--------|----------|-----------|--------------|
| POST | `/login` | Autentica usuário e cria sessão | Não |
| GET | `/logout` | Encerra a sessão do usuário | Sim |

### Usuários

| Método | Endpoint | Descrição | Autenticação |
|--------|----------|-----------|--------------|
| POST | `/user` | Cria um novo usuário | Não |
| GET | `/user/<id>` | Visualiza dados do usuário | Sim |
| PUT | `/user/<id>` | Atualiza senha do usuário | Sim |
| DELETE | `/user/<id>` | Deleta um usuário | Sim |

### Refeições

| Método | Endpoint | Descrição | Autenticação |
|--------|----------|-----------|--------------|
| POST | `/user/<id>/meals` | Adiciona uma nova refeição | Sim |
| GET | `/user/<id>/meals` | Lista todas as refeições do usuário | Sim |
| GET | `/user/<id_user>/meals/<id>` | Visualiza uma refeição específica | Sim |
| PUT | `/user/<id_user>/meals/<id>` | Atualiza uma refeição | Sim |
| DELETE | `/user/<id_user>/meals/<id>` | Deleta uma refeição | Sim |

## 💡 Exemplos de uso

### Criar um usuário
```bash
POST /user
Content-Type: application/json

{
  "username": "johndoe",
  "password": "senha123"
}
```

**Resposta:**
```json
{
  "message": "Usuário criado com sucesso"
}
```

### Fazer login
```bash
POST /login
Content-Type: application/json

{
  "username": "johndoe",
  "password": "senha123"
}
```

**Resposta:**
```json
{
  "message": "Autenticação realizada com sucesso"
}
```

### Adicionar uma refeição
```bash
POST /user/1/meals
Content-Type: application/json
Cookie: session=...

{
  "name": "Café da manhã",
  "description": "Ovos mexidos com pão integral",
  "date": "2024-02-04",
  "hour": "08:00",
  "inTheDiet": true
}
```

**Resposta:**
```json
{
  "message": "Refeição adicionada com sucesso"
}
```

### Listar todas as refeições
```bash
GET /user/1/meals
Cookie: session=...
```

**Resposta:**
```json
{
  "Meals": [
    {
      "name": "Café da manhã",
      "description": "Ovos mexidos com pão integral",
      "date": "2024-02-04",
      "hour": "08:00",
      "inTheDiet": true
    }
  ],
  "total meals": 1
}
```

### Atualizar uma refeição
```bash
PUT /user/1/meals/1
Content-Type: application/json
Cookie: session=...

{
  "name": "Café da manhã saudável",
  "description": "Ovos mexidos com pão integral e abacate",
  "date": "2024-02-04",
  "hour": "08:30",
  "inTheDiet": true
}
```

**Resposta:**
```json
{
  "message": "Refeição atualizada com sucesso"
}
```

### Deletar uma refeição
```bash
DELETE /user/1/meals/1
Cookie: session=...
```

**Resposta:**
```json
{
  "message": "Refeição deletada com sucesso"
}
```

## 🔒 Recursos de Segurança

- **bcrypt**: Hash de senhas com salt automático
- **Flask-Login**: Gerenciamento seguro de sessões
- **SQLAlchemy**: Proteção contra SQL Injection
- **Rotas protegidas**: Middleware de autenticação
- **Validação de permissões**: Usuários só podem acessar seus próprios dados
- **Sessões criptografadas**: Cookies seguros
- **Docker**: Isolamento do banco de dados

## 🔐 Regras de Negócio

- Usuários autenticados só podem visualizar/editar/deletar suas próprias refeições
- Usuários não podem deletar a própria conta se estiverem logados
- Senhas são sempre armazenadas com hash bcrypt
- Todas as rotas de refeições requerem autenticação
- Validação de proprietário em todas as operações de refeições

## 🐳 Comandos úteis do Docker
```bash
# Iniciar os containers
docker-compose up -d

# Ver logs do MySQL
docker-compose logs db

# Acessar o MySQL via linha de comando
docker exec -it <container_id> mysql -u root -p

# Parar os containers
docker-compose down

# Reiniciar os containers
docker-compose restart
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📄 Licença

Este projeto está sob a licença MIT.

## 👩‍💻 Autora

Desenvolvido por [Luisa Ferreira](https://github.com/luisaferreirass)

