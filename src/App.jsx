
import { Routes, Route } from 'react-router-dom'
import './App.css'
import Login from './auth/Login'
import Register from './auth/Register'
import NavBar from './components/NavBar'  
import Home from './pages/Home'
import AddParking from './Slice/AddParking'


function App() {
 

  return (
    <Routes>
      {/* <Route path='/' element={<NavBar />} /> */}
      <Route path='/' element={<Home />}/>
      <Route path='/login' element={<Login />} />
      <Route path='/register' element={<Register />} />
      <Route path='/parking' element={<AddParking />}/>
    </Routes>
  )
}

export default App
