//import packages and create a variable which is const throughout
const express=require('express');
const mongoose=require('mongoose');
const cors=require('cors');

//object for create a server
const app = express();
app.use(express.json());
app.use(cors());
//Schema for food collection
const foodSchema=new mongoose.Schema({
  name:String,
  calories:Number,
  protien:Number,
  carbs:Number,
  fats:Number,
  fibre:Number,
  weight:Number
})


const foodModel=new mongoose.model("foods",foodSchema);




//mongo connection
mongoose.connect("mongodb://127.0.0.1:27017/nutrition",{
  useNewUrlParser:true,
  useUnifiedTopology:true
})
.then(() =>{
  console.log("connected");
}) 
 //Route by which you access the functionality
 app.post("/food/create",(req,res)=>{
   //to view the data as body
   const food=req.body;
   //console.log(req.body);
   //to save the data on mongodb
   let foodObj=new foodModel(food);
   foodObj.save().then(()=>{
    //if mongodb save the data status will be updated on terminal
    res.send({status:"food stored"});
  })
})

app.get('/foods',async (req, res)=>{
  let foods=await foodModel.find();
  res.send({foods:foods});
})
// to handle the request
//app.get('/demo',(req,res)=>{
//  console.log("get request called");
//  res.send("response is done");
//})
//server will listen the perticular port number
app.listen(8000);