from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    rentals = db.relationship('Rental', backref='user', lazy=True)
    cart_items = db.relationship('Cart', backref='user', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(64))
    model = db.Column(db.String(64))
    year = db.Column(db.Integer)
    capacity = db.Column(db.String(64))
    fuel_type = db.Column(db.String(64))
    fuel_consumption = db.Column(db.String(64))
    transmission = db.Column(db.String(64))
    rental_price = db.Column(db.String(64))
    image_path = db.Column(db.String(128))
    rentals = db.relationship('Rental', backref='car', lazy=True)
    cart_items = db.relationship('Cart', backref='car', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'capacity': self.capacity,
            'fuel_type': self.fuel_type,
            'fuel_consumption': self.fuel_consumption,
            'transmission': self.transmission,
            'rental_price': self.rental_price,
            'image_path': self.image_path
        }

class Rental(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(64), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'car_id': self.car_id,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'total_price': self.total_price,
            'status': self.status
        }

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
    added_date = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'car_id': self.car_id,
            'added_date': self.added_date
        }
