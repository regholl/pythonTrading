from flask import Flask, render_template

app = Flask(__name__) # Creates an instance of the Flask Object


@app.route('/') # -> Specifies a webpage with the given uri(i = index), returns the object returned from the function
def home():
    return render_template('home.html')

@app.route('/landing-page/')
def layout():
    return render_template('layout.html')


if __name__ == '__main__': # If this is the main method
    app.run(debug=True) # run the app, when debug=True is passed through you can edit and restart the webpage without stopping the app

