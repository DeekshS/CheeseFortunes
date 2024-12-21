from flask import Flask, render_template, send_from_directory

# Create the app inside a function
def create_app():
    app = Flask(__name__)

    # Register routes
    @app.route('/')
    def index():
        return render_template('index.html')

    # Add a route to serve the sitemap
    @app.route('/sitemap.xml')
    def sitemap():
        return send_from_directory(app.root_path, 'sitemap.xml', mimetype='application/xml')

    return app

# Only run the app if this script is executed directly
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

