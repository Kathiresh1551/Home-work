from flask import Flask, render_template

app = Flask(__name__)

@app.route('/employeeDetails')
def calculator():
    return render_template('userDetails.html')

@app.route('/employees')
def employees():
    emp = [
        {"salutation": "Mr", "Name": "Kathiresh", "lastName": "C", "phoneNumber": "123456789", "occupation": "FrontEnd Developer"},
    ]
    return emp

@app.route('/employee')
def employee():
    emp = {"salutation": "Mr", "Name": "Kathiresh", "lastName": "C", "phoneNumber": "123456789", "occupation": "FrontEnd Developer"}

    return emp
app.run()
