import React from "react";

/**
 * ContactList component to display a list of contacts.
 * @param {Object} props - The component props.
 * @param {Array} props.contacts - An array of contact objects.
 * @param {Function} props.updateContact - Function to handle updating a contact.
 * @param {Function} props.updateCallback - Callback function to execute after an update.
 * @returns {React.JSX} The ContactList component.
 */
const ContactList = ({ contacts, updateContact, updateCallback }) => {

    /**
     * Handles deletion of a contact.
     * @param {number} id - The ID of the contact to delete.
     * @returns {void}
     */
    const onDelete = async (id) => {
        try {
            const options = {
                method: "DELETE"
            };
            const response = await fetch(`http://127.0.0.1:5000/delete_contact/${id}`, options);
            if (response.status === 200) {
                updateCallback();
            } else {
                console.error("Failed to Delete");
            }
        } catch (error) {
            alert(error);
        }
    };

    return (
        <div>
            <header>Contacts</header>
            <table>
                <thead>
                    <tr>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Email</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {contacts.map((contact) => (
                        <tr key={contact.id}>
                            <td>{contact.firstName}</td>
                            <td>{contact.lastName}</td>
                            <td>{contact.email}</td>
                            <td>
                                <button onClick={() => updateContact(contact)}>Update</button>
                                <button onClick={() => onDelete(contact.id)}>Delete</button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default ContactList;
