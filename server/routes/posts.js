import express from 'express';
import {getPosts,createPost,updatePost,deletePost,getPost,updatePostAvl} from '../controllers/posts.js'
const router = express.Router();

// localhost:5000/posts
//
//As a skateboard borrower, I want to see a list of available boards
router.get('/', getPosts);

router.get('/:id',getPost);

//As a skateboard owner I want to be able to add my individual board to a skateboard sharing marketplace.
router.post('/', createPost);

//As a skateboard owner I want to be able to indicate that my board is available or unavailable for sharing
router.patch('/avl/:id',updatePostAvl);
//As a skateboard owner I want to be able to modify the details for the board that I share.
router.patch('/:id',updatePost);

router.delete('/:id',deletePost);
export default router;