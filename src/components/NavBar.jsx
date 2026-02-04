import React from 'react'
import { Link } from 'react-router-dom'
import '../style/NavBar.css'

function NavBar({showLinks= true}) {
  return (
   <nav className='navbar'>
    <div className='links'>
      <h1 className='title'>Parking System</h1>

      {showLinks &&(
        <>

          <Link className ="register" to='/register'>Register</Link>
          <Link className ="login" to='/login'>Login</Link>
        </>
      )}

    </div>
   </nav>
  )
}

export default NavBar