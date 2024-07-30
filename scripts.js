document.addEventListener('DOMContentLoaded', () => {
    const carContainer = document.querySelector('.car-container');
    const carDetailsModal = document.getElementById('car-details-modal');
    const rentalDetailsModal = document.getElementById('rental-details-modal');
    const cartModal = document.getElementById('cart-modal');
    const cartItemsContainer = document.getElementById('cart-items');
    const cartCount = document.getElementById('cart-count');
    const loginModal = document.getElementById('login-modal');
    const signupModal = document.getElementById('signup-modal');
    const closeCarDetails = carDetailsModal.querySelector('.close');
    const closeRentalDetails = rentalDetailsModal.querySelector('.close');
    const closeCartModal = cartModal.querySelector('.close');
    const closeLoginModal = loginModal.querySelector('.close');
    const closeSignupModal = signupModal.querySelector('.close');
    const rentNowBtn = document.getElementById('rent-btn');
    const confirmRentBtn = document.getElementById('confirm-rent-btn');
    const paymentMethodSelect = document.getElementById('payment-method');
    const mpesaForm = document.getElementById('mpesa-form');
    const paypalForm = document.getElementById('paypal-form');
    const equityForm = document.getElementById('equity-form');

    let selectedCar = null;
    let cart = JSON.parse(localStorage.getItem('cart')) || [];

    const cars = [
        {
            id: 1,
            title: 'Toyota RAV4',
            year: '2021',
            people: '4 People',
            fuel: 'Hybrid',
            efficiency: '6.1km / 1-litre',
            transmission: 'Automatic',
            price: '$50 / day',
            img: 'rav4/hero_image_rav4hybrid.png'
        },
        {
            id: 2,
            title: 'Audi A4',
            year: '2022',
            people: '5 People',
            fuel: 'Petrol',
            efficiency: '10.5km / 1-litre',
            transmission: 'Automatic',
            price: '$60 / day',
            img: 'Audi A4 /a4-exterior-left-front-three-quarter-3.webp'
        },
        {
            id: 3,
            title: 'Mercedes-Benz C-Class',
            year: '2023',
            people: '5 People',
            fuel: 'Petrol',
            efficiency: '9.8km / 1-litre',
            transmission: 'Automatic',
            price: '$70 / day',
            img: 'mercedes-benz/009-2022-Mercedes-Benz-C300.webp'
        },
        {
            id: 4,
            title: 'G-Wagon',
            year: '2022',
            people: '5 People',
            fuel: 'Petrol',
            efficiency: '7.5km / 1-litre',
            transmission: 'Automatic',
            price: '$100 / day',
            img: 'G-Wagon/mercedes-amg-g63-2021-01-angle--exterior--front--red.jpg'
        },
        {
            id: 5,
            title: 'Subaru Outback',
            year: '2021',
            people: '5 People',
            fuel: 'Petrol',
            efficiency: '8.0km / 1-litre',
            transmission: 'Automatic',
            price: '$55 / day',
            img: 'Subaru Outback/outback+sport+xt.jpg'
        },
        {
            id: 6,
            title: 'Classic Convertible',
            year: '1965',
            people: '2 People',
            fuel: 'Petrol',
            efficiency: '12.0km / 1-litre',
            transmission: 'Manual',
            price: '$80 / day',
            img: 'Classic Convertible/1965-ford-mustang-convertible (1).jpeg'
        }
    ];

    function renderCars() {
        carContainer.innerHTML = "";
        cars.forEach(car => {
            const carCard = document.createElement('div');
            carCard.className = 'car-card';
            carCard.innerHTML = `
                <img src="${car.img}" alt="${car.title}">
                <div class="details">
                    <h3>${car.title}</h3>
                    <p>${car.year}</p>
                    <p>${car.people}</p>
                    <p>${car.fuel}</p>
                    <p>${car.efficiency}</p>
                    <p>${car.transmission}</p>
                    <p>${car.price}</p>
                </div>
                <div class="buttons">
                    <button class="love" data-id="${car.id}">❤️</button>
                    <button class="rent-now" data-id="${car.id}">Rent Now</button>
                </div>
            `;

            carCard.querySelector('.love').addEventListener('click', function() {
                this.classList.toggle('loved');
                addToCart(car.id);
            });

            carCard.querySelector('.rent-now').addEventListener('click', () => {
                selectedCar = car;
                showCarDetails(car);
            });

            carContainer.appendChild(carCard);
        });
    }

    function renderCart() {
        cartItemsContainer.innerHTML = "";
        cart.forEach(car => {
            const cartItem = document.createElement('div');
            cartItem.classList.add('cart-item');
            cartItem.innerHTML = `
                <img src="${car.img}" alt="${car.title}" class="cart-item-image">
                <div class="cart-item-details">
                    <span>${car.title}</span>
                    <button class="delete-btn" data-id="${car.id}">Delete</button>
                </div>
            `;
            cartItemsContainer.appendChild(cartItem);
        });
        cartCount.textContent = cart.length;
    }

    function addToCart(carId) {
        if (!cart.find(car => car.id === carId)) {
            const car = cars.find(car => car.id === carId);
            cart.push(car);
            localStorage.setItem('cart', JSON.stringify(cart));
            renderCart();
        }
    }

    function removeFromCart(carId) {
        cart = cart.filter(car => car.id !== carId);
        localStorage.setItem('cart', JSON.stringify(cart));
        renderCart();
    }

    function showCarDetails(car) {
        document.getElementById('car-title').textContent = car.title;
        document.getElementById('car-details').innerHTML = `
            <p>Year: ${car.year}</p>
            <p>Seats: ${car.people}</p>
            <p>Fuel: ${car.fuel}</p>
            <p>Efficiency: ${car.efficiency}</p>
            <p>Transmission: ${car.transmission}</p>
            <p>Price: ${car.price}</p>
        `;
        carDetailsModal.style.display = 'block';

        rentNowBtn.onclick = () => {
            document.getElementById('rental-car-title').textContent = car.title;
            rentalDetailsModal.querySelector('#rental-details').innerHTML = `
                <p>Car: ${car.title}</p>
                <p>Year: ${car.year}</p>
                <p>Seats: ${car.people}</p>
                <p>Fuel: ${car.fuel}</p>
                <p>Efficiency: ${car.efficiency}</p>
                <p>Transmission: ${car.transmission}</p>
                <p>Price: ${car.price}</p>
                <div>
                    <label for="pickup-location">Pickup Location:</label>
                    <input type="text" id="pickup-location">
                </div>
                <div>
                    <label for="pickup-date">Pickup Date:</label>
                    <input type="date" id="pickup-date">
                </div>
                <div>
                    <label for="pickup-time">Pickup Time:</label>
                    <input type="time" id="pickup-time">
                </div>
                <div>
                    <label for="dropoff-location">Dropoff Location:</label>
                    <input type="text" id="dropoff-location">
                </div>
                <div>
                    <label for="dropoff-date">Dropoff Date:</label>
                    <input type="date" id="dropoff-date">
                </div>
                <div>
                    <label for="dropoff-time">Dropoff Time:</label>
                    <input type="time" id="dropoff-time">
                </div>
                <div>
                    <label for="payment-method">Select Payment Method:</label>
                    <select id="payment-method" required>
                        <option value="">Choose...</option>
                        <option value="mpesa">M-Pesa</option>
                        <option value="paypal">PayPal</option>
                        <option value="equity">Equity Bank</option>
                    </select>
                </div>
            `;
            carDetailsModal.style.display = 'none';
            rentalDetailsModal.style.display = 'block';
        };
    }

    function closeModals() {
        carDetailsModal.style.display = 'none';
        rentalDetailsModal.style.display = 'none';
        cartModal.style.display = 'none';
        loginModal.style.display = 'none';
        signupModal.style.display = 'none';
    }

    closeCarDetails.addEventListener('click', closeModals);
    closeRentalDetails.addEventListener('click', closeModals);
    closeCartModal.addEventListener('click', closeModals);
    closeLoginModal.addEventListener('click', closeModals);
    closeSignupModal.addEventListener('click', closeModals);

    window.addEventListener('click', (event) => {
        if (event.target === carDetailsModal || event.target === rentalDetailsModal || event.target === cartModal || event.target === loginModal || event.target === signupModal) {
            closeModals();
        }
    });

    paymentMethodSelect.addEventListener('change', function () {
        const selectedMethod = this.value;
        document.querySelectorAll('.payment-form').forEach(form => form.style.display = 'none');
        
        if (selectedMethod === 'mpesa') {
            mpesaForm.style.display = 'block';
        } else if (selectedMethod === 'paypal') {
            paypalForm.style.display = 'block';
        } else if (selectedMethod === 'equity') {
            equityForm.style.display = 'block';
        }
    });

    confirmRentBtn.addEventListener('click', () => {
        const selectedMethod = paymentMethodSelect.value;
        if (selectedMethod === 'mpesa') {
            document.getElementById('mpesa-form').style.display = 'block';
        } else if (selectedMethod === 'paypal') {
            alert('PayPal payment is currently not implemented.');
        } else if (selectedMethod === 'equity') {
            alert('Equity Bank payment is currently not implemented.');
        } else {
            alert('Please select a payment method.');
        }
    });

    document.getElementById('mpesa-payment-form').addEventListener('submit', async (event) => {
        event.preventDefault();

        const phone = document.getElementById('mpesa-phone').value;
        const amount = document.getElementById('mpesa-amount').value;

        const response = await fetch('/initiate-payment', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ phone: phone, amount: amount })
        });

        const data = await response.json();

        if (data.ResponseCode === '0') {
            document.getElementById('payment-status').textContent = 'Payment initiated. Check your phone to complete the transaction.';
        } else {
            document.getElementById('payment-status').textContent = `Payment failed: ${data.errorMessage}`;
        }
    });

    document.addEventListener("click", function(event) {
        if (event.target.classList.contains("love")) {
            const carId = parseInt(event.target.dataset.id);
            addToCart(carId);
        }

        if (event.target.classList.contains("delete-btn")) {
            const carId = parseInt(event.target.dataset.id);
            removeFromCart(carId);
        }

        if (event.target.classList.contains("close")) {
            event.target.closest(".modal").style.display = "none";
        }
    });

    document.getElementById("cart-btn").addEventListener("click", function() {
        cartModal.style.display = "block";
    });

    document.getElementById("login-btn").addEventListener("click", function() {
        loginModal.style.display = "block";
    });

    document.getElementById("signup-btn").addEventListener("click", function() {
        signupModal.style.display = "block";
    });

    document.getElementById("login-form").addEventListener("submit", function(event) {
        event.preventDefault();
        // Implement login functionality here
        alert("Logged in successfully!");
        loginModal.style.display = "none";
    });

    document.getElementById("signup-form").addEventListener("submit", function(event) {
        event.preventDefault();
        // Implement sign-up functionality here
        alert("Signed up successfully!");
        signupModal.style.display = "none";
    });

    renderCars();
    renderCart();
});
