from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from sqlalchemy.sql import text
from config.database import db

app = Flask(__name__)

# Load environment variables from .env
load_dotenv('.env')

# Configure the SQLAlchemy URI
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_DATABASE')}"

# Initialize SQLAlchemy with the app
# db = SQLAlchemy(app)
db.init_app(app)

# Test the database connection (optional)
@app.route('/')
def index():
    try:
        with app.app_context():
            db.session.execute(text("SELECT 1"))
        return "Database connection successful!"
    except Exception as e:
        return f"Database connection failed: {str(e)}"

# Import and register blueprints or routes here
from routes.players import players_bp
app.register_blueprint(players_bp, url_prefix='/api/players')

# Error handling middleware (optional)
@app.errorhandler(500)
def internal_server_error(e):
    return "Internal Server Error", 500

# Function to create tables
def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)

