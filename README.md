# Reusable Dash in Flask Template
1. This is a template for a Flask app that allows routing to an embedded Dash application.
2. Run app.py to initialize the application. This both initiates the Dasha application and its required callbacks, as well as the Flask server.
3. The logic of the dash application is contained within the dash_app folder.
4. All Dash callbacks have to be contained within the function integrate_callbacks(app) in pltoly_dash/dash_app/index.py.