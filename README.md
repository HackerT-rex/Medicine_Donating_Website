# Medicine_Donating_Website
PDL_Project


from flask import *
import sqlite3
import csv


app = Flask(__name__)
# Function to save form data to a CSV file
def buyer_save_to_csv(data):
    with open('buyer_form_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data.values())


def donar_save_to_csv(data):
    with open('donar_form_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data.values())


def login_save_to_csv(data):
    with open('login_form_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data.values())

def signup_save_to_csv(data):
    with open('signup_form_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data.values())

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the buyer form
@app.route('/buyer.html', methods=['GET', 'POST'])
def buyer():
    if request.method == 'POST':
        buyer_save_to_csv(request.form)
        return redirect(url_for('home'))
    return render_template('buyer.html')

# Route for the donor form
@app.route('/donar.html', methods=['GET', 'POST'])
def donor():
    if request.method == 'POST':
        donar_save_to_csv(request.form)
        return redirect(url_for('home'))
    return render_template('donar.html')

# Route for the login form
@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_save_to_csv(request.form)
        return redirect(url_for('home'))
    return render_template('login.html')

# Route for the signup form
@app.route('/signup.html', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        signup_save_to_csv(request.form)
        return redirect(url_for('home'))
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)




from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

class FormHandler:
    def __init__(self, filename):
        self.filename = filename

    def save_to_csv(self, data):
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data.values())

class BuyerFormHandler(FormHandler):
    def __init__(self):
        super().__init__('buyer_form_data.csv')

class DonorFormHandler(FormHandler):
    def __init__(self):
        super().__init__('donor_form_data.csv')

class LoginFormHandler(FormHandler):
    def __init__(self):
        super().__init__('login_form_data.csv')

class SignupFormHandler(FormHandler):
    def __init__(self):
        super().__init__('signup_form_data.csv')

buyer_form_handler = BuyerFormHandler()
donor_form_handler = DonorFormHandler()
login_form_handler = LoginFormHandler()
signup_form_handler = SignupFormHandler()

class Routes:
    @staticmethod
    @app.route('/')
    def home():
        return render_template('home.html')

    @staticmethod
    @app.route('/buyer.html', methods=['GET', 'POST'])
    def buyer():
        if request.method == 'POST':
            buyer_form_handler.save_to_csv(request.form)
            return redirect(url_for('home'))
        return render_template('buyer.html')

    @staticmethod
    @app.route('/donor.html', methods=['GET', 'POST'])
    def donor():
        if request.method == 'POST':
            donor_form_handler.save_to_csv(request.form)
            return redirect(url_for('home'))
        return render_template('donor.html')

    @staticmethod
    @app.route('/login.html', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            login_form_handler.save_to_csv(request.form)
            return redirect(url_for('home'))
        return render_template('login.html')

    @staticmethod
    @app.route('/signup.html', methods=['GET', 'POST'])
    def signup():
        if request.method == 'POST':
            signup_form_handler.save_to_csv(request.form)
            return redirect(url_for('home'))
        return render_template('signup.html')

Routes()

if __name__ == '__main__':
    app.run(debug=True)
