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
