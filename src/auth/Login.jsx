import { useState } from "react"
import NavBar from "../components/NavBar"
import { useNavigate } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { login } from "./authSlice"
import '../style/Login.css'
function Login() {
  const [loginData, setLogin] = useState({
    username:"",
    password:""
  })
  const dispatch = useDispatch()
  const navigate = useNavigate()

const { user, isAuthanticated } = useSelector((state) => state.auth)
  const handellogin =(e) =>{
    setLogin({...loginData, [e.target.name] : e.target.value})
  }

  const loginFormSubmit = (e) => {
  e.preventDefault();

  if (!user) {
    alert("User not found! Please register first.");
    navigate("/register");
    return;
  }

  if (
    user.username === loginData.username &&
    user.password === loginData.password
  ) {
    dispatch(login(loginData));
    alert("Login Successful!");
    navigate("/parking");
  } else {
    alert("Invalid username or password. Please try again.");
  }
};
  return(

    <div >
      <NavBar showLinks={false}/>
      <div className="loginfield">
      <h1>Login Page</h1>
      <form onSubmit={loginFormSubmit} className="loginform">
          <input type="text" placeholder="Username" name="username" value ={loginData.username} onChange={handellogin} required/><br/>
          <input type="password" placeholder="Password" name="password" value ={loginData.password} onChange={handellogin} required/><br/>
          <button type="submit">Login</button>
      </form>
      </div>
    </div>
  )
}

export default Login
