import React from "react"

const ContantList = ({contacts}) => {
    return <div>
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
                    <tr key = {contactt.id}>
                        <td>{contact.firstName}</td>
                        <td>{contact.lastName}</td>
                        <td>{contact.email}</td>
                        <td>
                            <button>Update</button>
                            <button>Delete</button>
                        </td>
                </tr>
                ))}
            </tbody>
        </table>
    </div>
}

export default ContantList