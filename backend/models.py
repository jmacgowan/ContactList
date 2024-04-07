from config import db
from uuid import uuid4

class Contact(db.Model):
    """Represents a contact in the database."""

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), unique=False, nullable=False)
    last_name = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def to_json(self):
        """
        Convert the Contact object to a JSON dictionary.

        Returns:
            dict: A dictionary representation of the Contact object.
        """
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email
        }

def get_uuid():
    return uuid4.hex

class Users(db.model):
    __tablename__ = "users"
    id = db.Column(db.String(32), primary_key = True, unique = True, default = get_uuid)
    email = db.Column(db.String(128), unique = True)
    password = db.Column(db.Text, nullablle = False)



