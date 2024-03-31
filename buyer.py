from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('buyer.html')

@app.route('/buyer', methods=['POST'])
def submit():
    buyer_name = request.form['buyer_name']
    medicine_name = request.form['medicine_name']
    quantity = request.form['quantity']
    buyer_address = request.form['buyer_address']

    
    with open('buyer_records.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([buyer_name,buyer_address,medicine_name,quantity])

    return 'Medicine donation submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)

