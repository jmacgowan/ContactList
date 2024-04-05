import { useState } from "react";

const ContactForm = ({}) => {
    const [firstName, setFirstName] = useState("")
    const [lastName, setLastName] = useState("")
    const [email, setEmail] = useState("")
    
    return <form>
        <div>
            <label htmlFor="firstName">First Name: </label>
            <input type = "text" id = "firstName" value = {firstName} onChange={(e) => setFirstName(e.target.value)}/>
        </div>
    </form>
}