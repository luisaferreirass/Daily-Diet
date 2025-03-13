from flask import Flask, request, jsonify
from database import db
from models.meals import Meal
from models.user import User
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

login_manager = LoginManager()

db.init_app(app)
login_manager.init_app(app)

login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


#Rota de login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:

        user = User.query.filter_by(username=username).first()

        if user.password == password:
            login_user(user)
            print(current_user.is_authenticated)
            return jsonify({"message": "Autenticação realizada com sucesso"})

    return jsonify({"message": "Credenciais inválidas"}), 400  



#Rota de logout 
@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout realizado com sucesso"})



# Create user
@app.route('/user', methods=['POST'])
def create_user():
    data = request.json 
    username = data.get("username")
    password = data.get("password")

    if username and password:
        user = User(username= username, password= password)
        db.session.add(user)
        db.session.commit()
        return jsonify ({"message": "Usuário criado com sucesso"})
    
    if username:
        return jsonify ({"message": "Senha inválida"}), 404
    
    else:
        return jsonify ({"message": "Usuário inválido"}), 404
    


# Read user    
@app.route('/user/<int:id>', methods=['GET'])
@login_required
def get_user(id):
    user = User.query.get(id)
    
    if user:
        return {"username": user.username}
    
    return jsonify({"message": "Usuário não encontrado"})

# Update user 
@app.route('/user/<int:id>', methods=['PUT'])
@login_required
def update_user(id):
    user = User.query.get(id)
    data = request.json

    if user and id == current_user.id and data.get("password"):
        user.password = data.get("password")
        db.session.commit()
        return jsonify ({"message": "Dados atualizados com sucesso"})
    
    return jsonify({"message": "Usuário não encontrado"}), 404

# Delete user
@app.route('/user/<int:id>', methods=['DELETE'])
@login_required
def delete_user(id):
    user = User.query.get(id)

    if id == current_user.id:
        return jsonify({"message": "Não foi possível deletar esse usuário"}), 403

    if user:
        db.session.delete(user)
        db. it()
        return jsonify({"message": "Usuário deletado com sucesso"})
    
    return jsonify({"message": "Usuário não encontrado"}), 404


# Create meal
@app.route('/user/<int:id>/meals', methods= ['POST'])
@login_required
def create_meal(id):
    user = User.query.get(id)
    data = request.get_json()

    if id != current_user.id:
        return ({"message": "Não foi possível concluir essa operação"}), 404

    if user:
        meal = Meal(name=data.get("name"), description=data.get("description"), date=data.get("name"), hour=data.get("hour"), inTheDiet=data.get("inTheDiet"), id_user= user.id)
        db.session.add(meal)
        db.session.commit()
        return jsonify({"message": "Refeição adicionada com sucesso"})
    
    return jsonify({"message": "Usuário não encontrado"}), 404

# Read all meals
@app.route('/user/<int:id>/meals', methods=['GET'])
@login_required
def get_meals(id):
    user = User.query.get(id)

    if id != current_user.id:
        return ({"message": "Não foi possível concluir essa operação"}), 404

    if user:
        list_meals = Meal.query.filter(Meal.id_user == user.id).all()
        meals = []

        for m in list_meals:

            meal = {
                "name": m.name,
                "description": m.description,
                "date": m.date, 
                "hour": m.hour,
                "inTheDiet": m.inTheDiet
            }

            meals.append(meal)

        output = {
            "Meals": meals,
            "total meals": len(meals)
        }

        return jsonify(output)
    
    return jsonify({"message": "Usuário não encontrado"}), 404


# Read one meal
@app.route('/user/<int:id_user>/meals/<int:id>', methods=['GET'])
@login_required
def get_meal(id_user, id):
    user = User.query.get(id_user)
    meal = Meal.query.get(id)

    if id_user != current_user.id:
        return ({"message": "Não foi possível concluir essa operação"}), 404

    if user:

        if meal:

            return {
                "name": meal.name,
                "description": meal.description,
                "date": meal.date, 
                "hour": meal.hour,
                "inTheDiet": meal.inTheDiet
            }
        
        return jsonify({"message": "Refeição não encontrada"}), 404
    
    return jsonify({"message": "Usuário não encontrado"}), 404


#Uptade meal
@app.route('/user/<int:id_user>/meals/<int:id>', methods=['PUT'])
@login_required
def update_meal(id_user, id):
    user = User.query.get(id_user)
    meal = Meal.query.get(id)

    if id_user != current_user.id:
        return ({"message": "Não foi possível concluir essa operação"}), 404

    if user:

        if meal:
            data = request.get_json()
            
            meal.name = data["name"]
            meal.description = data["description"]
            meal.date = data["date"]
            meal.hour = data["hour"]
            meal.inTheDiet = data["inTheDiet"]

            db.sesson.commit()

            return jsonify({"message": "Refeição atualizada com sucesso"})
        
        return jsonify({"message": "Não foi possível encontar essa refeição"}), 404
    
    
    return jsonify({"message": "Usuário não encontrado"}), 404


#Delete meal
@app.route('/user/<int:id_user>/meals/<int:id>', methods=['DELETE'])
@login_required
def delete_meal(id_user, id):
    user = User.query.get(id_user)
    meal = Meal.query.get(id)

    if id_user != user.id:
        return ({"message": "Não foi possível concluir essa operação"}), 404

    if user:
       
        if meal:
            db.session.delete(meal)
            db.session.commit()
            
            return jsonify({"message": "Refeição deletada com sucesso"})
    
        return jsonify({"message": "Não foi possível encontar essa refeição"}), 404
    
    
    return jsonify({"message": "Usuário não encontrado"}), 404
            

if __name__ == '__main__':
    app.run(debug=True)