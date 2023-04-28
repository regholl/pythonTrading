from flask import Flask, render_template, request


######################## MAIN START #############################################################################################################################
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/users')
def view_user():
    return render_template('users.html')

@app.route('/security')
def view_security():
    return render_template('securities.html')

@app.route('/order')
def view_order():
    return render_template('users.html')

if __name__ == '__main__': # If this is the main method
    app.run(debug=True) # run the app, when debug=True is passed through you can edit and restart the webpage without stopping the app
######################## MAIN END ###############################################################################################################################