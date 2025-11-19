from flask import Flask
from models import db
import os

# Initialize the Flask application
app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Initialize database
db.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()
    print("Database tables created successfully!")

# Import routes AFTER app and db are fully initialized
# This must be at the end to avoid circular imports
from routes import *

if __name__ == '__main__':
    print("Starting Flask application...")
    print("Access the app at: http://127.0.0.1:5000/")
    app.run(debug=True, host='0.0.0.0', port=5000)