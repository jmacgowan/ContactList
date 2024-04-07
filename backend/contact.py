from flask import jsonify, request
from config import app, db
from models import Contact

# Route to get all contacts from the database
@app.route("/contacts", methods=["GET"])
def get_contacts():
    """
    Get all contacts from the database.

    Returns:
        jsonify: JSON response containing the list of contacts.
    """
    # Retrieve all contacts from the database
    contacts = Contact.query.all()

    # Convert contacts to JSON format
    json_contacts = [contact.to_json() for contact in contacts]
    return jsonify({"contacts": json_contacts})

# Route to create a new contact in the database
@app.route("/create_contact", methods=["POST"])
def add_contact():
    """
    Add a new contact to the database.

    Returns:
        jsonify: JSON response indicating the success or failure of the operation.
    """
    # Extract first name, last name, and email from request data
    data = request.json
    first_name = data.get("firstName")
    last_name = data.get("lastName")
    email = data.get("email")

    # Validate input data
    if not first_name or not last_name or not email:
        return jsonify({'message': 'Input a correctly formatted first name, last name, and email'}), 400

    try:
        # Create a new contact object
        new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
        # Add the new contact to the database
        db.session.add(new_contact)
        db.session.commit()
        return jsonify({'message': 'Contact added successfully'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400

# Route to update an existing contact in the database
@app.route("/update_contact/<int:id>", methods=["PATCH"])
def update_contact(id):
    """
    Update an existing contact in the database.

    Args:
        id (int): The ID of the contact to be updated.

    Returns:
        jsonify: JSON response indicating the success or failure of the operation.
    """
    contact = Contact.query.get(id)
    if not contact:
        return jsonify({'message': 'Input an existing record to update'}), 400

    data = request.json

    f_name = data.get("firstName", contact.first_name)
    l_name = data.get("lastName", contact.last_name)
    new_email = data.get("email", contact.email)
    
    if not f_name or not l_name or not new_email:
        return jsonify({'message': 'Input a correctly formatted first name, last name, and email'}), 400
    
    contact.first_name = f_name
    contact.last_name = l_name
    contact.email = new_email
    
    db.session.commit()

    return jsonify({'message': 'Contact updated successfully'}), 200

# Route to delete a contact from the database
@app.route("/delete_contact/<int:id>", methods=["DELETE"])
def delete_contact(id):
    """
    Delete a contact from the database.

    Args:
        id (int): The ID of the contact to be deleted.

    Returns:
        jsonify: JSON response indicating the success or failure of the operation.
    """
    # Retrieve the contact to be deleted from the database
    contact = Contact.query.get(id)
    if not contact:
        return jsonify({'Message': 'Contact not found'}), 404

    # Delete the contact from the database
    db.session.delete(contact)
    db.session.commit()

    return jsonify({'message': 'Contact deleted'}), 200

# Entry point to run the Flask application
if __name__ == "__main__":
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    # Run the Flask application in debug mode
    app.run(debug=True)