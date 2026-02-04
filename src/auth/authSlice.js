import { createSlice } from "@reduxjs/toolkit";


const initialState = {
  user : JSON.parse(localStorage.getItem('user')) || null,
  isAuthanticated : false,

}
export const authUser = createSlice({
  name : 'auth',
  initialState,
  reducers:{
    register: (state, action ) =>{
      state.user = action.payload
      localStorage.setItem('user', JSON.stringify(state.user))
    },
    logout :(state) =>{
      state.user = null 
      localStorage.removeItem('user')
    },
    login:(state, action) =>{
      const { username, password } = action.payload
      if(
        state.user &&
        state.user.username === username &&
        state.user.password === password
      ){
        // Login successful
        state.isAuthanticated = true;

      }else{
        // Login failed
        state.isAuthanticated = false;
      }

    }

  }

})
export const {register, login,logout} = authUser.actions
export default authUser.reducer
