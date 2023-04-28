from flask import Flask, render_template, request

app = Flask(__name__) # Creates an instance of the Flask Object


@app.route('/') # -> Specifies a webpage with the given uri(i = index), returns the object returned from the function
def home():
    print('1')
    return render_template('homepage.html')

# Homepage: Controlling the Buttons - Navigates to the Titled Page on the button
@app.route('/', methods=['POST'])
def ui_nav_buttons_hp(): # UI Navigation Buttons Homepage
    if request.method == 'POST': 
        if request.form.get('positions') == 'Positions': # Positions Button
            print('position_button')
            return render_template('positions.html')
        elif request.form.get('orders') == 'Orders': # Orders Button
            print('order_button')
            return render_template('orders.html')
        elif request.form.get('settings') == 'Settings':
            print('settings_button')
            return render_template('settings.html')
        else:
            print('step in at line 16')
            pass
    else:
        return render_template('home.html')
    
@app.route('/<pathname>/<id>', methods = ['POST', 'GET'])
def get_by_id():


if __name__ == '__main__': # If this is the main method
    app.run(debug=True) # run the app, when debug=True is passed through you can edit and restart the webpage without stopping the app

