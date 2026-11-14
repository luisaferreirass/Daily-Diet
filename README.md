# 🍽️ Daily Diet

## 📝 About the project

A complete REST API for daily diet management built with **Flask**, **Flask-Login** and **MySQL** containerized with **Docker**. The project implements a robust authentication system and full CRUD for logging and tracking meals, allowing users to monitor what they eat and check whether they are sticking to their diet.

Great for learning:
- Authentication with Flask-Login
- Table relationships (User-Meals)
- Full CRUD with protected routes
- Password hashing with bcrypt
- Containerization with Docker
- ORM with SQLAlchemy
- Per-user permission checks

## 🚀 Technologies used

- **Python 3.x**
- **Flask 2.3.0** - Web framework
- **Flask-SQLAlchemy 3.1.1** - Database ORM
- **Flask-Login 0.6.2** - Authentication and session management
- **bcrypt** - Password hashing
- **MySQL** - Relational database
- **Docker** - Database containerization
- **PyMySQL 1.1.0** - MySQL connector for Python
- **Werkzeug 2.3.0** - WSGI toolkit
- **Cryptography 41.0.7** - Cryptography library
- **Requests 2.31.0** - HTTP library

## ⚙️ How to run

### Prerequisites

- Python 3.x installed
- Docker and Docker Compose installed
- pip (Python package manager)

### Database Setup with Docker

1. Start the MySQL container using Docker Compose:
```bash
docker-compose up -d
```

2. Check that the container is running:
```bash
docker ps
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/luisaferreirass/Daily-Diet.git
cd Daily-Diet
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
```

3. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Install the dependencies:
```bash
pip install -r requirements.txt
```

### Running the application
```bash
python app.py
```

The API will be available at: `http://localhost:5000`

### Stopping the services
```bash
# Stop the MySQL container
docker-compose down

# Stop and remove volumes (deletes the data)
docker-compose down -v
```

## 🐳 Docker Configuration

### MySQL credentials (docker-compose.yml)
```yaml
MYSQL_USER: admin
MYSQL_PASSWORD: admin123
MYSQL_DATABASE: daily-diet
MYSQL_ROOT_PASSWORD: admin123
Port: 3307:3306
```

### Application connection
```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin123@127.0.0.1:3307/daily-diet'
```

## 🎯 Features

### User Management
- 📝 **Create** a user account
- 🔑 **Log in** with secure authentication
- 🚪 **Log out** to end the session
- 👤 **View** the user profile
- ✏️ **Update** the user's password
- 🗑️ **Delete** a user account

### Meal Management
- ➕ **Add** daily meals
- 📋 **List** all of the user's meals
- 🔍 **View** details of a specific meal
- ✏️ **Edit** meal information
- 🗑️ **Delete** meals
- ✅ **Mark** whether a meal is within the diet or not

## 🛠️ Data models

### User

| Field | Type | Description |
|-------|------|-----------|
| id | Integer | Primary key (auto-increment) |
| username | String | Username (unique) |
| password | String | Password hashed with bcrypt |

### Meal

| Field | Type | Description |
|-------|------|-----------|
| id | Integer | Primary key (auto-increment) |
| name | String | Meal name |
| description | String | Meal description |
| date | String | Meal date |
| hour | String | Meal time |
| inTheDiet | Boolean | Is it within the diet? |
| id_user | Integer | Foreign key (User) |

**Relationship:** A user can have many meals (1:N)

## 📸 API Endpoints

### Authentication

| Method | Endpoint | Description | Auth required |
|--------|----------|-----------|--------------|
| POST | `/login` | Authenticates the user and creates a session | No |
| GET | `/logout` | Ends the user's session | Yes |

### Users

| Method | Endpoint | Description | Auth required |
|--------|----------|-----------|--------------|
| POST | `/user` | Creates a new user | No |
| GET | `/user/<id>` | Shows user data | Yes |
| PUT | `/user/<id>` | Updates the user's password | Yes |
| DELETE | `/user/<id>` | Deletes a user | Yes |

### Meals

| Method | Endpoint | Description | Auth required |
|--------|----------|-----------|--------------|
| POST | `/user/<id>/meals` | Adds a new meal | Yes |
| GET | `/user/<id>/meals` | Lists all of the user's meals | Yes |
| GET | `/user/<id_user>/meals/<id>` | Shows a specific meal | Yes |
| PUT | `/user/<id_user>/meals/<id>` | Updates a meal | Yes |
| DELETE | `/user/<id_user>/meals/<id>` | Deletes a meal | Yes |

## 💡 Usage examples

### Create a user
```bash
POST /user
Content-Type: application/json

{
  "username": "johndoe",
  "password": "password123"
}
```

**Response:**
```json
{
  "message": "Usuário criado com sucesso"
}
```

### Log in
```bash
POST /login
Content-Type: application/json

{
  "username": "johndoe",
  "password": "password123"
}
```

**Response:**
```json
{
  "message": "Autenticação realizada com sucesso"
}
```

### Add a meal
```bash
POST /user/1/meals
Content-Type: application/json
Cookie: session=...

{
  "name": "Breakfast",
  "description": "Scrambled eggs with whole wheat bread",
  "date": "2024-02-04",
  "hour": "08:00",
  "inTheDiet": true
}
```

**Response:**
```json
{
  "message": "Refeição adicionada com sucesso"
}
```

### List all meals
```bash
GET /user/1/meals
Cookie: session=...
```

**Response:**
```json
{
  "Meals": [
    {
      "name": "Breakfast",
      "description": "Scrambled eggs with whole wheat bread",
      "date": "2024-02-04",
      "hour": "08:00",
      "inTheDiet": true
    }
  ],
  "total meals": 1
}
```

### Update a meal
```bash
PUT /user/1/meals/1
Content-Type: application/json
Cookie: session=...

{
  "name": "Healthy breakfast",
  "description": "Scrambled eggs with whole wheat bread and avocado",
  "date": "2024-02-04",
  "hour": "08:30",
  "inTheDiet": true
}
```

**Response:**
```json
{
  "message": "Refeição atualizada com sucesso"
}
```

### Delete a meal
```bash
DELETE /user/1/meals/1
Cookie: session=...
```

**Response:**
```json
{
  "message": "Refeição deletada com sucesso"
}
```

## 🔒 Security Features

- **bcrypt**: Password hashing with automatic salt
- **Flask-Login**: Secure session management
- **SQLAlchemy**: Protection against SQL Injection
- **Protected routes**: Authentication middleware
- **Permission checks**: Users can only access their own data
- **Encrypted sessions**: Secure cookies
- **Docker**: Database isolation

## 🔐 Business Rules

- Authenticated users can only view/edit/delete their own meals
- Users cannot delete their own account while logged in
- Passwords are always stored as bcrypt hashes
- All meal routes require authentication
- Ownership is validated on every meal operation

## 🐳 Useful Docker commands
```bash
# Start the containers
docker-compose up -d

# View MySQL logs
docker-compose logs db

# Access MySQL from the command line
docker exec -it <container_id> mysql -u root -p

# Stop the containers
docker-compose down

# Restart the containers
docker-compose restart
```

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 License

This project is licensed under the MIT License.

## 👩‍💻 Author

Developed by [Luisa Ferreira](https://github.com/luisaferreirass)
