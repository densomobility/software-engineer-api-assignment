The application code is present in the 'sharedassets' folder.<br />
<br />
INSTALLATION(Windows):<br />
<br />
Install Python 3.7.1<br />
Install the required packages with the below commands:<br />
pip install pytz==2018.7<br />
pip Django==2.1.3<br />
pip djangorestframework==3.9.2<br />
pip django-filter==2.1.0<br />
Clone the repository.<br />
Navigate to the location where "manage.py" file is present.<br />
To run the tests:<br />
command: python manage.py test<br />
To run the local server:<br />
command: python manage.py runserver<br />
<br />
<br />	
ASSUMPTIONS:<br />
<br />
- Website will be hosted on local machine.<br />
- "status" will be shown as "Available" if the "timestamp" column value is less than or equal to the time at which the request is made.<br />
Example:<br />
- If the "timestamp" column value is 2021-10-11 2pm and the API request is made at 2021-10-11 5pm then the "status" will be shown as "Available".<br />
- If the API request is made at 2021-10-11 10am then the "status" will be shown as "Not Available".<br />
Not considering timezone info. All times are considered as UTC.<br />
<br />
<br />
DJANGO FOLDER STRUCTURE:<br />
<br />
- The root directory(called project in Django) is named "sharedassets". It contains a folder(app) called "skateboard" where the main code is written.<br />
- The "models" folder in it, contains the database code, "tests" folder contains the testing code, "serializers" file defines the API content, "urls" files contains the routing configuration and the "views" file contains the business logic.<br />
<br />
<br />
HOW TO USE:<br />
<br />
Django provides built-in browsable API  to view, create, modify and delete the API data.<br />
- Root URL: http://127.0.0.1:8000/skateboard/api/<br />
- URL: http://127.0.0.1:8000/skateboard/api/skateboard/<br />
Click on the "Filters" button to filter the data based on ID, NAME_OWNER, BRAND, WEIGHT(min and max values can be specified), LENGTH(min and max values can be specified), LOCATION and STATUS.<br />
PATCH can be used as well to modify the data.<br />
DATA will be delivered in JSON format.<br />
The filtering choices for the "status" dropdown are "Available" and "Not Available" values.<br />
The filtering choices for the "brand" dropdown are "Baker", "Birdhouse" and "Krooked" values.<br />
Since built-in browsable API is provided, didn't create front-end.<br />
<br />
- GET List of available skateboards:<br />
   URL:http://127.0.0.1:8000/skateboard/api/skateboard/<br />
   Output:<br />
      List of skateboard records<br />
      ID(positive integer)<br />
      NAME_OWNER(string)<br />
      BRAND(string)<br />
      WEIGHT(float)<br />
      LENGTH(float)<br />
      LOCATION(string)<br />
      TIMESTAMP(string)<br />
      STATUS(string)<br />
<br />
- POST Create skateboard:<br />
   URL:http://127.0.0.1:8000/skateboard/api/skateboard/<br />
   Input:<br />
      At the bottom of the web page(http://127.0.0.1:8000/skateboard/api/skateboard/), enter the input as a HTML form or JSON data and click on the "POST" button.<br />
      Enter NAME_OWNER(string)<br />
      Enter BRAND(string) has to be one among "Baker", "Birdhouse" and "Krooked" values<br />
      Enter WEIGHT(float) >=2 and <=20<br />
      Enter LENGTH(float)	>=70 and <=90<br />
      Enter LOCATION(string)<br />
      Enter TIMESTAMP(string) in the order "YYYY-MM-DDThh:mm:ssZ"<br />
   Output:<br />
      ID(positive integer)<br />
      Entered NAME_OWNER(string)<br />
      Entered BRAND(string)<br />
      Entered WEIGHT(float)<br />
      Entered LENGTH(float)<br />
      Entered LOCATION(string)<br />
      Entered TIMESTAMP(string)<br />
      STATUS(string)<br />
<br />
- GET a particular skateboard based on ID:<br />
   URL:http://127.0.0.1:8000/skateboard/api/skateboard/ID/<br />
   Input: Numerical ID of the skateboard should be at the end of the URL<br />
   Output:<br />
      ID(positive integer)<br />
      NAME_OWNER(string)<br />
      BRAND(string)<br />
      WEIGHT(float)<br />
      LENGTH(float)<br />
      LOCATION(string)<br />
      TIMESTAMP(string)<br />
      STATUS(string)<br />
<br />
- GET skateboards based on weight less than a value:<br />
   URL:http://127.0.0.1:8000/skateboard/api/skateboard/?weight_lte=<value><br />
   Input: "weight_lte" query parameter and the weight value should be at the end of the URL<br />
   Output:<br />
      List of skateboard records for which the weight is less than or equal to the entered value<br />
      ID(positive integer)<br />
      NAME_OWNER(string)<br />
      BRAND(string)<br />
      WEIGHT(float)<br />
      LENGTH(float)<br />
      LOCATION(string)<br />
      TIMESTAMP(string)<br />
      STATUS(string)<br />
<br />
- PUT Update a particular skateboard:<br />
   URL:http://127.0.0.1:8000/skateboard/api/skateboard/ID/<br />
   Input: Numerical ID of the skateboard should be at the end of the URL.<br />
      At the bottom of the web page(http://127.0.0.1:8000/skateboard/api/skateboard/<ID>/), enter the input as a HTML form or JSON data and click on the "PUT" button.<br />
      Enter NAME_OWNER(string)<br />
      Enter BRAND(string) has to be one among "Baker", "Birdhouse" and "Krooked" values<br />
      Enter WEIGHT(float) >=2 and <=20<br />
      Enter LENGTH(float)	>=70 and <=90<br />
      Enter LOCATION(string)<br />
      Enter TIMESTAMP(string) in the order "YYYY-MM-DDThh:mm:ssZ"<br />
		Output:<br />
     ID(positive integer)<br />
     Entered NAME_OWNER(string)<br />
     Entered BRAND(string)<br />
     Entered WEIGHT(float)<br />
     Entered LENGTH(float)<br />
     Entered LOCATION(string)<br />
     Entered TIMESTAMP(string)<br />
     STATUS(string)<br />
<br />
- DELETE a particular skateboard:<br />
    URL:http://127.0.0.1:8000/skateboard/api/skateboard/ID/<br />
    Input: Numerical ID of the skateboard should be at the end of the URL. Click on the "DELETE" button to delete the current record.<br />
		
	
	
