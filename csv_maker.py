import csv

with open('buyer_form_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name','address','medicine_name','quantity'])

with open('donar_form_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name','address','medicine_name','quantity'])

with open('login_form_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name','password'])

with open('signup_form_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name','password'])

