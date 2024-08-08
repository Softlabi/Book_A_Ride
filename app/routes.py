from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/book')
def book():
    return render_template('book.html')

@main.route('/map')
def map():
    return render_template('map.html')

@main.route('/get-started')
def get_started():
    return render_template('get_started.html')

@main.route('/login')
def login():
    return render_template('login.html')

@main.route('/logout')
def logout():
    # Handle logout logic
    return redirect(url_for('main.index'))

@main.route('/client_home')
def client_home():
    return render_template('client_home.html')

@main.route('/driver_dashboard')
def driver_dashboard():
    return render_template('driver_dashboard.html')

@main.route('/ride_details/<ride_id>')
def ride_details(ride_id):
    # Fetch ride details from the database or other source based on ride_id
    # For example purposes, using static data
    ride_info = {
        'client_location': 'OAU Hostel One',
        'distance': '30 km',
        'time': '45 mins',
        'price': '$20'
    }
    return render_template('ride_details.html', ride_id=ride_id, **ride_info)

@main.route('/confirm_ride/<ride_id>', methods=['POST'])
def confirm_ride(ride_id):
    # Handle ride confirmation logic
    # Update ride status in the database or perform necessary actions
    print(f"Ride {ride_id} confirmed")
    return redirect(url_for('main.driver_dashboard'))

@main.route('/available_drivers', methods=['POST'])
def available_drivers():
    # Retrieve booking details from the form
    present_location = request.form['present_location']
    end_location = request.form['end_location']
    ride_time = request.form['ride_time']
    car_size = request.form['car_size']
    
    # Fetch available drivers based on booking details
    # Example static data, replace with actual database queries or API calls
    drivers = [
        {'id': 1, 'name': 'John Doe', 'phone': '08123456789', 'car_description': 'Toyota Camry 2020', 'price': '15'},
        {'id': 2, 'name': 'Jane Smith', 'phone': '09012345678', 'car_description': 'Honda Accord 2019', 'price': '18'}
    ]
    
    return render_template('available_drivers.html', drivers=drivers)

@main.route('/confirm_driver/<driver_id>', methods=['POST'])
def confirm_driver(driver_id):
    # Handle driver confirmation logic
    # Update booking with selected driver, etc.
    print(f"Driver {driver_id} confirmed")
    return redirect(url_for('main.client_home'))

@main.route('/submit_client', methods=['POST'])
def submit_client():
    name = request.form['name']
    location = request.form['location']
    phone = request.form['phone']
    email = request.form['email']
    # Process the form data as needed
    return redirect(url_for('main.client_home'))

@main.route('/submit_driver', methods=['POST'])
def submit_driver():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    driver_id = request.form['driver_id']
    plate_number = request.form['plate_number']
    # Process the form data as needed
    return redirect(url_for('main.driver_dashboard'))

@main.route('/login_user', methods=['POST'])
def login_user():
    role = request.form['role']
    email = request.form['email']
    password = request.form['password']
    # Validate login credentials
    if role == 'client':
        return redirect(url_for('main.client_home'))
    elif role == 'driver':
        return redirect(url_for('main.driver_dashboard'))
    return redirect(url_for('main.index'))

@main.route('/submit_booking', methods=['POST'])
def submit_booking():
    present_location = request.form['present_location']
    end_location = request.form['end_location']
    ride_time = request.form['ride_time']
    car_size = request.form['car_size']
    
    # Process the booking data
    # Redirect to the available drivers page
    return redirect(url_for('main.available_drivers', present_location=present_location, end_location=end_location, ride_time=ride_time, car_size=car_size))
