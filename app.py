from flask import Flask, render_template
from plotly_dash.dash_flask_integrator import init_dash

app = Flask(__name__)
DASH_APP_BASE_PATHNAME = '/dashboard'

@app.route('/')
def flask_home():
    return render_template('flask_home.html', DASH_APP_BASE_PATHNAME = DASH_APP_BASE_PATHNAME)

# Route to the Dash app
@app.route(f'{DASH_APP_BASE_PATHNAME}')
def dashboard():
    return

if __name__ == '__main__':
    init_dash(app, DASH_APP_BASE_PATHNAME)
    app.run(debug=False)
