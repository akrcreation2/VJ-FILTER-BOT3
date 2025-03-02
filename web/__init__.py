# Credit - adarsh-goel

from aiohttp import web
from web.stream_routes import routes  # Assuming routes is defined in stream_routes.py

# Create a new aiohttp Application
web_app = web.Application()

# Add routes to the application
web_app.add_routes(routes)

# Define the main entry point for the app
if __name__ == '__main__':
    # Run the application on a specific host and port (for example, localhost:8080)
    web.run_app(web_app, host='0.0.0.0', port=8080)
