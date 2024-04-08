from flask import jsonify, request
from werkzeug.exceptions import abort
from flask_bcrypt import Bcrypt
from config import app, db
from models import User 

@app.route("/register")
def register_user():
    email = request.json["email"]
    password = request.json["password"]
    hashed_password = bcrypt.generate_password_hash(password)

    user_exists = User.query.filter_by(email=email).first() is not None
    
    if user_exists:
        abort(409)
    
    new_user = User(email=email, password = hashed_password)
    db.session.add(new_user)
    db.session.commit()

    
    return jsonify({})
# Entry point to run the Flask application
if __name__ == "__main__":
    bcrypt = Bcrypt(app)
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    # Run the Flask application in debug mode
    app.run(debug=True)