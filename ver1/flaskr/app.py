from flask import Flask, render_template, request


######################## MAIN START #############################################################################################################################
app = Flask(__name__)

# a simple page that says hello

@app.route('/users')
def view_users():
    return render_template('users.html')



if __name__ == '__main__': # If this is the main method
    app.run(debug=True) # run the app, when debug=True is passed through you can edit and restart the webpage without stopping the app
######################## MAIN END ###############################################################################################################################