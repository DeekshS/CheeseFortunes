
from flask import Flask, render_template

# Create the app inside a function
def create_app():
    app = Flask(__name__)

    # Register routes
    @app.route('/')
    def index():
        return render_template('index.html')

    return app

# Only run the app if this script is executed directly
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
