//import logo from './logo.svg';
//import './App.css';
import {Container, AppBar, Typography, Grow, Grid} from '@material-ui/core';

import Posts from './components/Posts/Posts'
import Form from './components/Form/Form'
import skateboarders from './images/skateboarders.jpg';
const App = ()=> {
  return (
    <Container maxWidth="lg">
      <AppBar position="static" color="inherit">
        <Typography variant="h3" align="center">SkateBoard Market Place</Typography>
        <img src={skateboarders} alt="skateboarders" height="160"/>
      </AppBar>
      <Grow in>
        <Container>
          <Grid container justify="space-between" alignItems="stretch" spacing={3}>
            <Grid item xs={12} sm={7}>
              <Posts />
            </Grid>
            <Grid item xs={12} sm={4}>
              <Form /> 
            </Grid>
          </Grid>
        </Container>
      </Grow>
    </Container>
  );
}

export default App;
