from flask import Blueprint, request, jsonify, render_template
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..extensions import db
from ..models import Car, User

bp = Blueprint('cars', __name__, url_prefix='/cars')

@bp.route('/')
def index():
    return "Welcome to Baraka Travels!"

@bp.route('/all', methods=['GET'])
def get_cars():
    cars = Car.query.all()
    return jsonify([car.serialize() for car in cars]), 200

@bp.route('/add', methods=['POST'])
@jwt_required()
def add_car():
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user['username']).first()
    if not user.is_admin:
        return jsonify({'message': 'Admin access required'}), 403

    data = request.get_json()
    new_car = Car(
        title=data['title'],
        year=data['year'],
        people=data['people'],
        fuel=data['fuel'],
        efficiency=data['efficiency'],
        transmission=data['transmission'],
        price=data['price'],
        img=data['img']
    )
    db.session.add(new_car)
    db.session.commit()
    return jsonify({'message': 'Car added successfully'}), 201

@bp.route('/update/<int:car_id>', methods=['PUT'])
@jwt_required()
def update_car(car_id):
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user['username']).first()
    if not user.is_admin:
        return jsonify({'message': 'Admin access required'}), 403

    data = request.get_json()
    car = Car.query.get_or_404(car_id)
    car.title = data['title']
    car.year = data['year']
    car.people = data['people']
    car.fuel = data['fuel']
    car.efficiency = data['efficiency']
    car.transmission = data['transmission']
    car.price = data['price']
    car.img = data['img']
    car.available = data['available']
    db.session.commit()
    return jsonify({'message': 'Car updated successfully'}), 200

@bp.route('/delete/<int:car_id>', methods=['DELETE'])
@jwt_required()
def delete_car(car_id):
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user['username']).first()
    if not user.is_admin:
        return jsonify({'message': 'Admin access required'}), 403

    car = Car.query.get_or_404(car_id)
    db.session.delete(car)
    db.session.commit()
    return jsonify({'message': 'Car deleted successfully'}), 200
