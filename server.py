from flask import *
import csv

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the buyer form
@app.route('/buyer.html', methods=['GET', 'POST'])
def buyer():
    if request.method == 'POST':
        save_to_csv(request.form)
        return redirect(url_for('home'))
    return render_template('buyer.html')

# Route for the donor form
@app.route('/donar.html', methods=['GET', 'POST'])
def donor():
    if request.method == 'POST':
        save_to_csv(request.form)
        return redirect(url_for('home'))
    return render_template('donar.html')

# Route for the profile form
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        save_to_csv(request.form)
        return redirect(url_for('home'))
    return render_template('profile.html')

# Route for the login form
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        save_to_csv(request.form)
        return redirect(url_for('home'))
    return render_template('login.html')

# Route for the signup form
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        save_to_csv(request.form)
        return redirect(url_for('home'))
    return render_template('signup.html')

# Function to save form data to a CSV file
def save_to_csv(data):
    with open('form_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data.values())

if __name__ == '__main__':
    app.run(debug=True)
