import { React,useState,useEffect } from 'react';
import FileBase from 'react-file-base64';
import { useDispatch,useSelector } from 'react-redux';
import useStyles from './styles';
import { createPost,updatePost } from '../../actions/posts';
import { TextField,Button,Typography,Paper } from '@material-ui/core';
//import { updatePost } from '../../../../server/controllers/posts';
const Form = ({currentId,setCurrentId}) => {
    const [postData,setPostData]= useState({
        creator:'',title:'',message:'',selectedFile:'',board:{brand:'',weight:'',condition:'',price:''},location:{State:'',City:''},availability:''
    });
    const post = useSelector((state)=>currentId?state.posts.find((p)=>p._id === currentId):null);
    const classes = useStyles();
    const dispatch = useDispatch();

    useEffect(()=>{
        console.log(post);
        if(post) setPostData(post);
    },[post])

    const handleSubmit = (e)=>{
        e.preventDefault();
        if(currentId){
            console.log("attempting to update a post");
            dispatch(updatePost(currentId,postData));
        }
        else{
            console.log("attempting to create a post");
            dispatch(createPost(postData));
        }
        //setPostData({...postData,board:{...postData.board,weight:Number(postData.board.weight)}});
        //setPostData({...postData,board:{...postData.board,price:Number(postData.board.price)}});
        console.log(postData);
        
    }
    const clear = () =>{

    }

    return (
       <Paper className={classes.paper}>
           <form autoComplete='off' noValidate className={'${classes.root} ${classes.form}'} onSubmit={handleSubmit}>
                <Typography variant="h6">Creating a SkateBoard</Typography>
                <TextField name="creator" variant="outlined" label="Creator" fullWidth value={postData.creator} onChange={(e)=>setPostData({...postData,creator:e.target.value})}/>
                <TextField name="title" variant="outlined" label="Title" fullWidth value={postData.title} onChange={(e)=>setPostData({...postData,title:e.target.value})}/>
                <TextField name="message" variant="outlined" label="Message" fullWidth value={postData.message} onChange={(e)=>setPostData({...postData,message:e.target.value})}/>

                <TextField name="brand" variant="outlined" label="Brand" fullWidth value={postData.board.brand} onChange={(e)=>setPostData({...postData,board:{...postData.board,brand:e.target.value}})}/>
                <TextField name="weight" variant="outlined" label="Weight(lb)" fullWidth value={postData.board.weight} onChange={(e)=>setPostData({...postData,board:{...postData.board,weight:Number(e.target.value)}})}/>
                <TextField name="condition" variant="outlined" label="Condition" fullWidth value={postData.board.condition} onChange={(e)=>setPostData({...postData,board:{...postData.board,condition:e.target.value}})}/>
                <TextField name="price" variant="outlined" label="Price($)" fullWidth value={postData.board.price} onChange={(e)=>setPostData({...postData,board:{...postData.board,price:Number(e.target.value)}})}/>

                <TextField name="state" variant="outlined" label="State" fullWidth value={postData.location.State} onChange={(e)=>setPostData({...postData,location:{...postData.location,State:e.target.value}})}/>
                <TextField name="city" variant="outlined" label="City" fullWidth value={postData.location.City} onChange={(e)=>setPostData({...postData,location:{...postData.location,City:e.target.value}})}/>

                <TextField name="availability" variant="outlined" label="Availability" fullWidth value={postData.availability} onChange={(e)=>setPostData({...postData,availability:e.target.value})}/>
                <div className={classes.fileInput}>
                    <FileBase type='file' multiple={false} onDone={({base64})=>setPostData({...postData,selectedFile:base64})}/>
                </div>
                <Button className={classes.buttonSubmit} variant="contained" color="primary" size="large" type="submit" fullWidth>Submit</Button>
                <Button  variant="contained" color="secondary" size="small" onClick={clear} fullWidth>Clear</Button>
            </form>
       </Paper>
    );
} 

export default Form;