from app import create_app, db
from app.models import Car, User, Rental, Cart
from datetime import datetime

app = create_app()

with app.app_context():
    db.create_all()
    
    # Add initial cars
    cars = [
        ("Toyota RAV4", "2021", "4 People", "Hybrid", "6.1km / 1-litre", "Automatic", "$50 / day", "rav4/hero_image_rav4hybrid.png"),
        ("Audi A4", "2022", "5 People", "Petrol", "10.5km / 1-litre", "Automatic", "$60 / day", "Audi A4/a4-exterior-left-front-three-quarter-3.webp"),
        ("Mercedes-Benz C-Class", "2023", "5 People", "Petrol", "9.8km / 1-litre", "Automatic", "$70 / day", "mercedes-benz/009-2022-Mercedes-Benz-C300.webp"),
        ("G-Wagon", "2022", "5 People", "Petrol", "7.5km / 1-litre", "Automatic", "$100 / day", "G-Wagon/mercedes-amg-g63-2021-01-angle--exterior--front--red.jpg"),
        ("Subaru Outback", "2021", "5 People", "Petrol", "8.0km / 1-litre", "Automatic", "$55 / day", "Subaru Outback/outback+sport+xt.jpg"),
        ("Classic Convertible", "1965", "2 People", "Petrol", "12.0km / 1-litre", "Manual", "$80 / day", "Classic Convertible/1965-ford-mustang-convertible (1).jpeg")
    ]

    for car_data in cars:
        car = Car(make=car_data[0], model=car_data[1], year=int(car_data[2]), capacity=car_data[3], fuel_type=car_data[4], fuel_consumption=car_data[5], transmission=car_data[6], rental_price=car_data[7], image_path=car_data[8])
        db.session.add(car)
    
    # Add initial users
    users = [
        {"username": "john_doe", "email": "john@example.com", "password": "hashed_password", "is_admin": False},
        {"username": "jane_smith", "email": "jane@example.com", "password": "hashed_password", "is_admin": False},
        {"username": "alice_jones", "email": "alice@example.com", "password": "hashed_password", "is_admin": False},
        {"username": "bob_brown", "email": "bob@example.com", "password": "hashed_password", "is_admin": False},
        {"username": "charlie_davis", "email": "charlie@example.com", "password": "hashed_password", "is_admin": False}
    ]

    for user_data in users:
        user = User(**user_data)
        db.session.add(user)

    db.session.commit()
    
    # Add initial rentals
    rentals = [
        {"user_id": 1, "car_id": 1, "start_date": datetime(2024, 8, 1), "end_date": datetime(2024, 8, 5), "total_price": 200, "status": "booked"},
        {"user_id": 2, "car_id": 2, "start_date": datetime(2024, 8, 6), "end_date": datetime(2024, 8, 10), "total_price": 300, "status": "booked"},
        {"user_id": 3, "car_id": 3, "start_date": datetime(2024, 8, 11), "end_date": datetime(2024, 8, 15), "total_price": 350, "status": "booked"},
        {"user_id": 4, "car_id": 4, "start_date": datetime(2024, 8, 16), "end_date": datetime(2024, 8, 20), "total_price": 500, "status": "booked"},
        {"user_id": 5, "car_id": 5, "start_date": datetime(2024, 8, 21), "end_date": datetime(2024, 8, 25), "total_price": 275, "status": "booked"}
    ]

    for rental_data in rentals:
        rental = Rental(**rental_data)
        db.session.add(rental)
    
    # Add initial cart items
    cart_items = [
        {"user_id": 1, "car_id": 1, "added_date": datetime.utcnow()},
        {"user_id": 2, "car_id": 2, "added_date": datetime.utcnow()},
        {"user_id": 3, "car_id": 3, "added_date": datetime.utcnow()},
        {"user_id": 4, "car_id": 4, "added_date": datetime.utcnow()},
        {"user_id": 5, "car_id": 6, "added_date": datetime.utcnow()}
    ]

    for cart_item_data in cart_items:
        cart_item = Cart(**cart_item_data)
        db.session.add(cart_item)

    db.session.commit()
    print("Database seeded!")
