from flask import Blueprint, request, jsonify
from . import db
from .models import User, Car, Rental
from datetime import datetime
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return "Welcome to Baraka Travels Car Rental!"

@bp.route('/cars', methods=['GET'])
def get_cars():
    cars = Car.query.all()
    return jsonify([car.to_dict() for car in cars])

@bp.route('/car', methods=['POST'])
def add_car():
    data = request.get_json()
    new_car = Car(
        make=data['make'],
        model=data['model'],
        year=data['year'],
        seats=data['seats'],
        engine=data['engine'],
        fuel_efficiency=data['fuel_efficiency'],
        transmission=data['transmission'],
        rental_price=data['rental_price'],
        image_url=data['image_url']
    )
    db.session.add(new_car)
    db.session.commit()
    return jsonify(new_car.to_dict()), 201

@bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

@bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    user = User.query.filter_by(username=data['username'], password=data['password']).first()
    if user:
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Invalid credentials"}), 401

@bp.route('/rentals', methods=['POST'])
@jwt_required()
def rent_car():
    user_id = get_jwt_identity()
    data = request.get_json()
    new_rental = Rental(
        user_id=user_id,
        car_id=data['car_id'],
        start_date=data['start_date'],
        end_date=data['end_date'],
        total_price=data['total_price'],
        status=data['status']
    )
    db.session.add(new_rental)
    db.session.commit()
    return jsonify(new_rental.to_dict()), 201

@bp.route('/my_rentals', methods=['GET'])
@jwt_required()
def get_my_rentals():
    user_id = get_jwt_identity()
    rentals = Rental.query.filter_by(user_id=user_id).all()
    return jsonify([rental.to_dict() for rental in rentals])

@bp.route('/cart', methods=['POST'])
@jwt_required()
def add_to_cart():
    user_id = get_jwt_identity()
    data = request.get_json()
    new_cart_item = Cart(user_id=user_id, car_id=data['car_id'], added_date=datetime.utcnow())
    db.session.add(new_cart_item)
    db.session.commit()
    return jsonify(new_cart_item.to_dict()), 201

@bp.route('/cart', methods=['GET'])
@jwt_required()
def get_cart():
    user_id = get_jwt_identity()
    cart_items = Cart.query.filter_by(user_id=user_id).all()
    return jsonify([item.to_dict() for item in cart_items])
