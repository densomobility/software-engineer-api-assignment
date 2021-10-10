import {Card,CardActions,CardContent,CardMedia,Button,Typography} from '@material-ui/core';
//import ThumbUpAltIcon from '@material-ui/core';
import DeleteIcon from '@material-ui/icons/Delete';
import MoreHorizIcon from '@material-ui/icons/MoreHoriz';
import moment from 'moment';
import useStyles from './styles';
const Post = ({post,setCurrentId}) => {
    const classes = useStyles();
    return (
        <Card className={classes.card}>
            <CardMedia className={classes.media} image={post.selectedFile} title={post.title}/>
            <div className={classes.overlay}>
                <Typography variant='h6'>{post.creator}</Typography>
                <Typography variant='h5'>${post.board.price}</Typography>
                <Typography variant='body2'>{moment(post.createdAt).fromNow()}</Typography>
            </div>
            <div className={classes.overlay2}>
                <Button style={{color:'white'}} size='small' onclick={()=>setCurrentId(post._id)}>
                    <MoreHorizIcon fontSize='default' />
                </Button>
            </div>
            <div className={classes.details}>
                <Typography variant='body2' color='textSecondary'>{post.board.brand}</Typography>
                <Typography variant='body2' color='textSecondary'>{post.board.condition}</Typography>
            </div>
            <CardContent className={classes.title}>
                <Typography variant='h5' gutterBottom>{post.message}</Typography>
            </CardContent>
            <CardActions>
                <Button size='small' color='primary' onClick={()=>{} }>
                    <DeleteIcon frontSize="small" />
                    Delete
                </Button>
            </CardActions>
        </Card>
            
    );
} 

export default Post;