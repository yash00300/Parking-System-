import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  parkingSport: JSON.parse(localStorage.getItem('parkingSport')) || []
};


export const parking = createSlice({
  name : 'parking',
  initialState,
  reducers:{
    addParking : (state, action) =>{
      console.log("Stored:", action.payload);// remove later
      state.parkingSport.push(action.payload)
      localStorage.setItem('parkingSport', JSON.stringify(state.parkingSport))
    },

  }
})

export const {addParking} = parking.actions
export default parking.reducer
