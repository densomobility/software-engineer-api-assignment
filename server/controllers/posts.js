//import express from 'express';
import  mongoose  from 'mongoose';
import PostMessage from '../models/postMessage.js';

export const getPosts = async (req,res)=>{
   // res.send('this works!');
   try{
    const postMessages = await PostMessage.find({ availability : "Available" },{});

    res.status(200).json(postMessages);
   }catch(error){
        res.status(404).json({message:error.message});
   }

}

export const createPost = async (req,res)=>{
    //res.send('Post Creattion');
    const post = req.body;
    const newPost = new PostMessage(post);
    try{
        await newPost.save();
        res.status(201).json(newPost);
    }catch(error){
        res.status(409).json({message:error.message});
    }
}

export const updatePost = async (req,res)=>{
    const {id:_id} = req.params;
    const post = req.body;
    if(!mongoose.Types.ObjectId.isValid(_id)) return res.status(404).send('No post with that id');

    const updatedPost = await PostMessage.findByIdAndUpdate(_id,  {...post, _id},{new:true})

    res.json(updatedPost);
}

export const updatePostAvl = async (req,res)=>{
    const {id:_id} = req.params;
    const post = req.body;
    console.log(post.availability);
    if(!mongoose.Types.ObjectId.isValid(_id)) return res.status(404).send('No post with that id');

    try{
        const updatedPost = await PostMessage.updateOne({_id},{$set:{availability:post.availability}})
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
    console.log(id);
    try{
        const post = await PostMessage.findById(id);
        //console.log(postMessage);
        res.status(200).json(post);
       }catch(error){
            res.status(404).json({message:error});
       }
    console.log('GETBYID!');

}