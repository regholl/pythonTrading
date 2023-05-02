import os

from flask import Flask, render_template, request


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route('/')
    def homepage(): 
        return render_template('home.html')
    
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
                print('step in at line 25')
                pass
        else:
            return render_template('home.html')
    
    from . import db
    db.init_app(app)

    return app
