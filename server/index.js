import express from 'express';
import mongoose from 'mongoose';
import cors from 'cors';

const app = express();
app.use(express.urlencoded({extended: true}));
app.use(express.json()) // To parse the incoming requests with JSON payloads

app.unsubscribe(cors());

const CONNECTION_URL ='mongodb+srv://jbcostan:P%40ssw0rd!@cluster0.fs5ci.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
const PORT = process.env.PORT || 5000;

mongoose.connect(CONNECTION_URL,{useNewUrlParser: true, useUnifiedTopology: true})
.then(()=>app.listen(PORT,()=>console.log('Server runnning on port: ${PORT}')))
.catch((error)=>console.log(error.message));
