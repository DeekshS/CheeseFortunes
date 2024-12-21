from flask import Flask, render_template, Response

# Create the app inside a function
def create_app():
    app = Flask(__name__)

    # Register routes
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/sitemap.xml')
    def sitemap():
        # Sitemap XML content
        sitemap_content = """<?xml version="1.0" encoding="UTF-8"?>
        <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
            http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
        <url>
            <loc>https://cheeseeightball.onrender.com/</loc>
            <lastmod>2024-12-21T21:46:01+00:00</lastmod>
        </url>
        </urlset>"""
        # Return the sitemap with the correct XML content type
        return Response(sitemap_content, mimetype='application/xml')

    return app

# Only run the app if this script is executed directly
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
