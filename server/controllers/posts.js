//import express from 'express';
import  mongoose  from 'mongoose';
import PostMessage from '../models/postMessage.js';

export const getPosts = async (req,res)=>{
   console.log("Atempting to get all available posts")
   try{
    const postMessages = await PostMessage.find({ availability : "Available" },{});
    console.log("found:"+ postMessages.length);
    res.status(200).json(postMessages);
   }catch(error){
       console.log(error);
        res.status(404).json({message:error.message});
   }

}

export const createPost = async (req,res)=>{
    //res.send('Post Creattion');
    const post = req.body;
    const newPost = new PostMessage(post);
    console.log("Atempting to get all available posts")
    try{
        await newPost.save();
        console.log("added successful")
        res.status(201).json(newPost);
    }catch(error){
        console.log(error);
        res.status(409).json({message:error.message});
    }
}

export const updatePost = async (req,res)=>{
    console.log(req.params)
    console.log("Atempting to update post")
    const {id:_id} = req.params;
    const post = req.body;
    if(!mongoose.Types.ObjectId.isValid(_id)) return res.status(404).send('No post with that id');

    const updatedPost = await PostMessage.findByIdAndUpdate(_id,  {...post, _id},{new:true})
    console.log("update successful")
    res.json(updatedPost);
}

export const updatePostAvl = async (req,res)=>{
    const {id:_id} = req.params;
    const post = req.body;
    console.log(post.availability);
    if(!mongoose.Types.ObjectId.isValid(_id)) return res.status(404).send('No post with that id');

    try{
        const updatedPost = await PostMessage.updateOne({_id},{$set:{availability:post.availability}})
        console.log("update successful")
        res.json(updatedPost);
    }catch(error){

    }

}

export const deletePost = async(req,res)=>{
    const{id} = req.params;
    if(!mongoose.Types.ObjectId.isValid(id)) return res.status(404).send('No post with that id');
    await PostMessage.findByIdAndRemove(id);
    console.log('DELETE!');
    res.json({message:"Post deleted successfully"})
}

export const getPost = async(req,res)=>{
    const{id} = req.params;
    if(!mongoose.Types.ObjectId.isValid(id)) return res.status(404).send('No post with that id');
    console.log("Atempting to get single post with id:"+id);
    try{
        const post = await PostMessage.findById(id);
        console.log("found:"+post.owner);
        res.status(200).json(post);
       }catch(error){
            res.status(404).json({message:error});
       }
    console.log('GETBYID!');

}