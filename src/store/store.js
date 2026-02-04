import { configureStore } from "@reduxjs/toolkit";
import { authUser } from "../auth/authSlice";
import { parking } from "../Slice/parkingSlice";

export const store = configureStore({
  reducer:{
    auth : authUser.reducer,
    park : parking.reducer,
  },
})