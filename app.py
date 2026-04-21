from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.task_routes import task_bp

app = Flask(__name__)

# Database config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Make db available everywhere
from models.task import Task

app.register_blueprint(task_bp)

@app.route("/")
def home():
    return "Smart Task Manager API is running 🚀"

# Create DB tables
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
