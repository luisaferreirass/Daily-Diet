from database import db

class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    hour = db.Column(db.String(50), nullable=False)
    inTheDiet = db.Column(db.Boolean, nullable=False)
    id_user = db.Column(db.Integer)

  
        