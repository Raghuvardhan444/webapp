from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define the root route
@app.route('/')
def home():
    return "Hello, World!"

# Define an additional endpoint for demonstration
@app.route('/about')
def about():
    return "This is a simple web application built with Flask."

# Run the application
if __name__ == '__main__':
    app.run(debug=True, port=5000)
