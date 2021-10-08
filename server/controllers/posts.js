import PostMessage from '../models/postMessage.js';

export const getPosts = async (req,res)=>{
   // res.send('this works!');
   try{
    const postMessages = await PostMessage.find();

    res.status(200).json(postMessages);
   }catch(error){
        res.status(404).json({message:error.message});
   }

}

export const createPost = async (req,res)=>{
    //res.send('Post Creattion');
    const newPost = new PostMessage(post);
    try{
        await newPost.save();
        res.status(201).json(newPost);
    }catch(err){
        res.status(409).json({message:error.message});
    }
}