# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')  # Main landing page

# @app.route('/about')
# def about():
#     return render_template('aboutus.html')  # About Us page

# @app.route('/booking')
# def booking():
#     return render_template('booking.html')  # Booking Details page

# @app.route('/addservice')
# def add_service():
#     return render_template('addservice.html')  # Add Service page

# @app.route('/registration')
# def registration():
#     return render_template('registration.html')  # Registration page

# @app.route('/login')
# def login():
#     return render_template('loginpage.html')  # Login page

# @app.route('/venue')
# def venue_booking():
#     return render_template('venue.html')  # Venue Booking page

# @app.route('/catering')
# def catering_services():
#     return render_template('catering.html')  # Catering Services page

# @app.route('/eventplanning')
# def event_planning():
#     return render_template('eventplanning.html')  # Event Planning page

# @app.route('/transportation')
# def transportation():
#     return render_template('transportation.html')  # Transportation page

# @app.route('/decoration')
# def decoration_services():
#     return render_template('decoration.html')  # Decoration Services page

# @app.route('/entertainment')
# def entertainment():
#     return render_template('entertainment.html')  # Entertainment page

# if __name__ == '__main__':
#     app.run(debug=True)


import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Load chatbot responses from JSON file
def load_responses():
    with open("responses.json", "r") as file:
        return json.load(file)

responses = load_responses()

@app.route("/")
def home():
    return render_template("chatbot.html")

@app.route("/chatbot", methods=["POST"])
def chatbot():
    user_message = request.json.get("message", "").lower()
    
    # Get response from JSON database or default message
    response = responses.get(user_message, responses["default"])
    
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)

