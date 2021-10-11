import mongoose from 'mongoose';

const postSchema = mongoose.Schema({
    title:String,
    message:String,
    createdAt:{
        type:Date,
        default: new Date()
    },
    creator:String,
    board:{
        brand:String,
        weight:Number,
        condition:String,
        price:Number
    },
    location:{
        State:String,
        City:String
    },
    availability:String,
    selectedFile:String

});

const PostMessage = mongoose.model('PostMessage',postSchema);
export default PostMessage;