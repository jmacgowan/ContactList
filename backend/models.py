from config import db

class Contact(db.Model):
    __tablename__ = 'contacts'  

    """Represents a contact in the database."""

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), unique=False, nullable=False)
    last_name = db.Column(db.String(50), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=False, nullable=False)

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
