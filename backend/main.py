from flask import jsonify, request
from config import app, db
from models import Contact

@app.route("/contacts", methods = ["GET"])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x:x.to_json(), contacts))
    return jsonify({"contacts" : json_contacts})

@app.route("/create_contact", methods=["POST"])
def add_contacts():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or not last_name or not email:
        return jsonify({'message': 'Input a correctly formatted first name, last name, and email'}), 400

    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
    try:
        db.session.add(new_contact)
        db.session.commit()
        return jsonify({'message': 'Contact added successfully'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route("/update_contact/<int:id>", methods=["PATCH"])
def update_contacts(id):
    contact = Contact.query.get(id)
    if not contact:
        return (jsonify({'message' : 'Input an existing record to update'},
        400))
    data = request.json

    f_name = data.get("firstName", contact.first_name)
    print(f_name)
    l_name = data.get("lastName", contact.last_name)
    new_email = data.get("email", contact.email)
    
    if not f_name or not l_name or not new_email:
        return jsonify({'message': 'Input a correctly formatted first name, last name, and email'}), 400
    
    contact.first_name = f_name
    contact.last_name = l_name
    contact.email = new_email
    
    db.session.commit()

    return jsonify({'message' : 'usr updated'}, 200)

@app.route("/delete_contact/<int:id>", methods=["DELETE"])
def delete_contact(id):
    contact = Contact.query.get(id)
    if not contact:
        return jsonify({'Message': 'User not found'}), 404

    db.session.delete(contact)
    db.session.commit()

    return jsonify({'message': 'User deleted'}), 200
    
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug = True)
