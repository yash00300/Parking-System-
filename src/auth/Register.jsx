import { useState } from "react"
import NavBar from "../components/NavBar"
import { useNavigate } from "react-router-dom"
import { useDispatch } from "react-redux"
import { register } from "./authSlice"
import '../style/Register.css'

function Register(){
  const navigate = useNavigate()
  const [formdata, setFormdata] = useState({
    firstName:"", 
    lastName:"",
    username:"",
    number:"",
    email:"",
    password:"",
    conformPassword:""
  })
  const dispatch = useDispatch()

  const handelRegister =(e)=>{
    setFormdata({...formdata, [e.target.name]:e.target.value})
  }
  const registerform = (e) =>{
    e.preventDefault();
    if (formdata.password !== formdata.conformPassword ){
      alert("Password and Confirm Password do not match!");
      return;
    }

    if(formdata.password.length < 8){
      alert("Password must be at least 8 characters long.");
    }

    if(
      !(
    formdata.email.includes('@gmail.com') ||
    formdata.email.includes('@gmail.in')
  )
    ){
      alert("Please enter a valid email address.");
      return;
    }

    dispatch(register(formdata))
    console.log(formdata)
    navigate('/login')

  }


  return(

    <div>
      <NavBar showLinks={false}/>
      <div className="registerForm">
        <h1>Register Page</h1>
        <form onSubmit={registerform}>
          <input type="text" placeholder="First Name" name="firstName" value={formdata.firstName} onChange={handelRegister} required/><br/>
          <input type="text" placeholder="Last Name" name="lastName" value={formdata.lastName}  onChange={handelRegister} required/><br/>
          <input type="text" placeholder="Username" name="username" value={formdata.username}  onChange={handelRegister} required/><br/>
          <input type="text" placeholder="Number" name="number" value={formdata.number}  onChange={handelRegister} required/><br/>
          <input type="email" placeholder="Email" name="email" value={formdata.email}  onChange={handelRegister} required/><br/>
          <input type="password" placeholder="Password" name="password" value={formdata.password}  onChange={handelRegister} required/><br/>
          <input type="password" placeholder="conform Password" name="conformPassword" value={formdata.conformPassword}  onChange={handelRegister} required/><br/>
          <button type="submit">Register</button>
        </form>

      </div>

    </div>
  )
}
export default Register