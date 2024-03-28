from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('your_webpage.html')

@app.route('/submit', methods=['POST'])
def submit():
    medicine_name = request.form['medicine_name']
    quantity = request.form['quantity']
    
    with open('medicine_donations.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([medicine_name, quantity])

    return 'Medicine donation submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)

