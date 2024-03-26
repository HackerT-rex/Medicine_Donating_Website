from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def order_form():
    if request.method == 'POST':
        buyer_name = request.form['buyer_name']
        buyer_address = request.form['buyer_address']
        medicine_name = request.form['medicine_name']
        quantity = request.form['quantity']

        # Do something with the form data, for example, print it
        print("Buyer Name:", buyer_name)
        print("Buyer Address:", buyer_address)
        print("Medicine Name:", medicine_name)
        print("Quantity:", quantity)

        # Return a response indicating the form was submitted
        return "Order placed successfully!"

    # Render the HTML template containing the form
    return render_template('buyer.html')

if __name__ == '__main__':
    app.run(debug=True)
