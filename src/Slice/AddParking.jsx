import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import { addParking } from "./parkingSlice";
import NavBar from "../components/NavBar";
function AddParking(){
  const [carData, setcarData] = useState({
    carName : '',
    carNumber: '',
    carOwner : '',
  })

  const dispatch = useDispatch();
  const navigate = useNavigate();
  const handleParking=(e) =>{
    setcarData({...carData, [e.target.name]: e.target.value})
  }
  console.log(carData)
  const handleSubmit = (e) =>{
    e.preventDefault();

    // Dispatch action to add parking slot
    dispatch(addParking(carData))
    // Navigate to another page if needed
    navigate('/')

  }

    const parkingList = useSelector(state => state.park.parkingSport)
    const alerthandler = parkingList.some(
    car => car.carNumber === carData.carNumber
    );

    if (alerthandler) {
    alert("Parking Slot already exists!");
    return;
    }
    console.log(parkingList)

  return(
    <div>
      <NavBar showLinks={false}/>
      <h1>Add Parking Slot</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="Car name" name="carName" value={carData.carName} onChange={handleParking}/>
        <br/>
        <input type="text" placeholder="Car Number" name="carNumber" value={carData.carNumber} onChange={handleParking}/>
        <br/>
        <input type="text" placeholder="Car Owner" name="carOwner" value={carData.carOwner} onChange={handleParking}/>
        <br/>
        <button type="submit">Add Parking</button>

      </form>
    </div>
  );
}
export default AddParking