# software-engineer-api-assignment

### Skateboard REST API

In this assignment I decided to go with the MERN stack technology.  I went with Heroku as my cloud application platform and Netlify to host my front-end.
Link to my front-end:https://clever-ardinghelli-a6b180.netlify.app/
link to the api:https://skateboard-rest-api.herokuapp.com/

### Server Side
**Instructions for Deployment**
This instruction is ment for deploying my server directory to Heroku, but the same logic can be applied to any cloud application platform. I've also provided the production-ready api above.


Install the Heroku CLI
Download and install the Heroku CLI.

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.

$ heroku login
Clone the repository
Use Git to clone skateboard-rest-api's source code to your local machine.

$ heroku git:clone -a skateboard-rest-api
$ cd skateboard-rest-api
Deploy your changes
Make some changes to the code you just cloned and deploy them to Heroku using Git.

$ git add .
$ git commit -am "make it better"
$ git push heroku master


### Client Side
**Instructions for Deployment**

To run the client in localhost, make sure to have nodejs installed.
Change directory to the client and run npm install to install all modules listed in dependencies.
See above for the client's link 

### Using the API with Postman
I will break it down per user stories

**As a skateboard borrower, I want to see a list of available boards**
Use GET to https://skateboard-rest-api.herokuapp.com/posts

Screenshot:https://prnt.sc/1vo3bgm

**As a skateboard owner I want to be able to add my individual board to a skateboard sharing marketplace.**
Use POST to https://skateboard-rest-api.herokuapp.com/posts
In the body, choose JSON and follow format below (add your own base64 string)
	
	{
        "board": {
            "brand": "Metroller",
            "weight": 11,
            "condition": "New",
            "price": 35
        },
        "location": {
            "State": "Michigan",
            "City": "Detriot"
        },
        "_id": "61637ab676cd9a9cbba79a56",
        "title": "Metroller Advance",
        "message": "Standard Skate Boards (Advance)",
        "createdAt": "2021-10-10T04:02:12.112Z",
        "creator": "Amazon",
        "availability": "Available",
        "selectedFile": "base64 string here",
        "__v": 0
    }

![Screenshot](https://prnt.sc/1vo4lvy)

**As a skateboard owner I want to be able to indicate that my board is available or unavailable for sharing**
Use PATCH to https://skateboard-rest-api.herokuapp.com/posts/avl/61637ab676cd9a9cbba79a56  (where the last parameter is a mongodb id )
In the body, choose JSON and follow format below (change to Available or UnAvailable)
Screenshot:https://prnt.sc/1vo53xk

**As a skateboard owner I want to be able to modify the details for the board that I share.**
Use PATCH to https://skateboard-rest-api.herokuapp.com/posts/61637ab676cd9a9cbba79a56  (where the last parameter is a mongodb id )
In the body, choose JSON and follow format similar to adding a new board
Screenshot:https://prnt.sc/1vo64ro

**Extra: As a skateboard owner I want to see a specific board**
Use GET to https://skateboard-rest-api.herokuapp.com/posts/61637ab676cd9a9cbba79a56
Screenshot:https://prnt.sc/1vo754v

**Extra: As a skateboard owner I want to delete any of my board**
Use DELETE https://skateboard-rest-api.herokuapp.com/posts/61637ab676cd9a9cbba79a56 (where the last parameter is a mongodb id )
Screenshot:https://prnt.sc/1vo6tgk

Keep in mind that the mongodb id's here might have been deleted already, please create a post and use it's id to do the test.

### Using the API with the client
headover to https://clever-ardinghelli-a6b180.netlify.app/ or install locally using the direction I mentioned earlier

I will break it down per user stories

**As a skateboard borrower, I want to see a list of available boards**
The homePage will only show skateboards that has availability property set to "Available"
Screenshot:https://prnt.sc/1vo7nmw

**As a skateboard owner I want to be able to add my individual board to a skateboard sharing marketplace.**
Use the form at the right side and fill in the input box and choose file, then press submit
Screenshot:https://prnt.sc/1vo86m9

**As a skateboard owner I want to be able to indicate that my board is available or unavailable for sharing**
click the 3 white dots on a specific post, the form will change from 'Creating a SkateBoard' to  'Editing a skateBoard'
and will autofill the form for you. To change availability, simply change Availability inputbox to either 'Available' or 'UnAvailable'
Screenshot:https://prnt.sc/1vo8ath

**As a skateboard owner I want to be able to modify the details for the board that I share.**
The same procedure above


**Extra: As a skateboard owner I want to delete any of my board**
pick a post and simply click delete



**What is this?**
This is my solution to the Skateboard API REST Assignment
