import mongoose from 'mongoose';

const postSchema = mongoose.Schema({
    title:String,
    message:String,
    user: {
        firstName: String,
        lastName: String,
        createdAt:{
            type:Date,
            default: new Date()
        }
    },
    board:{
        owner:{
            firstName: String,
            lastName: String
        },
        brand:String,
        weight:Number,
        location:{
            State:String,
            City:String
        },
        age:{
            type:Date,
            default: new Date()
        },
        condition:String
    }

});

const PostMessage = mongoose.model('PostMessage',postSchema);
export default PostMessage;