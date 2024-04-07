import React, { useState, useEffect } from 'react';
import ContactList from './ContactList';
import './App.css';
import ContactForm from './ContactForm';

/**
 * App component representing the main application.
 * @returns {JSX.Element} The App component.
 */
function App() {
  const [contacts, setContacts] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [currentContact, setCurrentContact] = useState({});

  /**
   * Fetches the list of contacts from the server.
   * @returns {void}
   */
  useEffect(() => {
    fetchContacts();
  }, []);

  /**
   * Fetches the list of contacts from the server.
   * @returns {void}
   */
  const fetchContacts = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/contacts");
      const data = await response.json();
      setContacts(data.contacts);
      console.log(data.contacts);
    } catch (error) {
      console.error("Failed to fetch contacts:", error);
    }
  };

  /**
   * Closes the modal.
   * @returns {void}
   */
  const closeModal = () => {
    setIsModalOpen(false);
    setCurrentContact({});
  };

  /**
   * Opens the modal to create a new contact.
   * @returns {void}
   */
  const openCreateModal = () => {
    if (!isModalOpen) setIsModalOpen(true);
  };

  /**
   * Opens the modal to edit a contact.
   * @param {Object} contact - The contact to be edited.
   * @returns {void}
   */
  const openEditModal = (contact) => {
    if (isModalOpen) return;
    setCurrentContact(contact);
    setIsModalOpen(true);
  };

  /**
   * Callback function to execute after updating a contact.
   * @returns {void}
   */
  const onUpdate = () => {
    closeModal();
    fetchContacts();
  };

  return (
    <>    
      <ContactList contacts={contacts} updateContact={openEditModal} updateCallback={onUpdate}/>
      <button onClick={openCreateModal}>Create New Contact</button>
      {isModalOpen && <div className='modal'>
        <div className='modal-content'>
          <span className='close' onClick={closeModal}>&times;</span>
          <ContactForm existingContact={currentContact} updateCallback={onUpdate}/>
        </div>
        </div>}
    </>
  );
}

export default App;
