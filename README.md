The application code is present in the 'sharedassets' folder.

INSTALLATION(Windows):

Install Python 3.7.1
Install the required packages:
   pip install pytz==2018.7
	  pip Django==2.1.3
	  pip djangorestframework==3.9.2
	  pip django-filter==2.1.0
Clone the repository.
Navigate to the location where "manage.py" file is present.
To run the tests:
	  python manage.py test
To run the local server:
	  python manage.py runserver

	
ASSUMPTIONS:

Website will be hosted on local machine.
"status" will be shown as "Available" if the "timestamp" column value is less than or equal to the time at which the request is made.
Example:
	  If the "timestamp" column value is 2021-10-11 2pm and the API request is made at 2021-10-11 5pm then the "status" will be shown as "Available".
	  If the API request is made at 2021-10-11 10am then the "status" will be shown as "Not Available".
Not considering timezone info. All times are considered as UTC.


DJANGO FOLDER STRUCTURE:

The root directory(called project in Django) is named "sharedassets". It contains a folder(app) called "skateboard" where the main code is written.
The "models" folder in it, contains the database code, "tests" folder contains the testing code, "serializers" file defines the API content, "urls" files contains the routing configuration and the "views" file contains the business logic. 


HOW TO USE:
	
Django provides built-in browsable API  to view, create, modify and delete the API data.
   Root URL: http://127.0.0.1:8000/skateboard/api/
	  URL: http://127.0.0.1:8000/skateboard/api/skateboard/
Click on the "Filters" button to filter the data based on ID, NAME_OWNER, BRAND, WEIGHT(min and max values can be specified), LENGTH(min and max values can be specified), LOCATION and STATUS.
PATCH can be used as well to modify the data.
DATA will be delivered in JSON format.
The filtering choices for the "status" dropdown are "Available" and "Not Available" values.
The filtering choices for the "brand" dropdown are "Baker", "Birdhouse" and "Krooked" values.
Since built-in browsable API is provided, didn't create front-end.
	
GET List of available skateboards:
   URL:http://127.0.0.1:8000/skateboard/api/skateboard/
   Output:
      List of skateboard records
      ID(positive integer) 
      NAME_OWNER(string)
      BRAND(string)
      WEIGHT(float)
      LENGTH(float)
      LOCATION(string)
      TIMESTAMP(string)
      STATUS(string)
		
POST Create skateboard:
   URL:http://127.0.0.1:8000/skateboard/api/skateboard/
   Input:
      At the bottom of the web page(http://127.0.0.1:8000/skateboard/api/skateboard/), enter the input as a HTML form or JSON data and click on the "POST" button.
      Enter NAME_OWNER(string)
      Enter BRAND(string) has to be one among "Baker", "Birdhouse" and "Krooked" values
      Enter WEIGHT(float) >=2 and <=20
      Enter LENGTH(float)	>=70 and <=90
      Enter LOCATION(string)
      Enter TIMESTAMP(string) in the order "YYYY-MM-DDThh:mm:ssZ"
   Output:
      ID(positive integer) 
      Entered NAME_OWNER(string)
      Entered BRAND(string)
      Entered WEIGHT(float)
      Entered LENGTH(float)
      Entered LOCATION(string)
      Entered TIMESTAMP(string)
      STATUS(string)
			
GET a particular skateboard based on ID:
		 URL:http://127.0.0.1:8000/skateboard/api/skateboard/<ID>/
		 Input: ID of the skateboard should be at the end of the URL
		 Output:
      ID(positive integer)
      NAME_OWNER(string)
      BRAND(string)
      WEIGHT(float)
      LENGTH(float)
      LOCATION(string)
      TIMESTAMP(string)
      STATUS(string)
			
GET skateboards based on weight less than a value:
		URL:http://127.0.0.1:8000/skateboard/api/skateboard/?weight_lte=<value>
		Input: "weight_lte" query parameter and the weight value should be at the end of the URL
		Output:
      List of skateboard records for which the weight is less than or equal to the entered value
      ID(positive integer)
      NAME_OWNER(string)
      BRAND(string)
      WEIGHT(float)
      LENGTH(float)
      LOCATION(string)
      TIMESTAMP(string)
      STATUS(string)
			
PUT Update a particular skateboard:
		 URL:http://127.0.0.1:8000/skateboard/api/skateboard/<ID>/
		 Input: ID of the skateboard should be at the end of the URL.
      At the bottom of the web page(http://127.0.0.1:8000/skateboard/api/skateboard/<ID>/), enter the input as a HTML form or JSON data and click on the "PUT" button.
      Enter NAME_OWNER(string)
      Enter BRAND(string) has to be one among "Baker", "Birdhouse" and "Krooked" values
      Enter WEIGHT(float) >=2 and <=20
      Enter LENGTH(float)	>=70 and <=90
      Enter LOCATION(string)
      Enter TIMESTAMP(string) in the order "YYYY-MM-DDThh:mm:ssZ"
		Output:
     ID(positive integer) 
     Entered NAME_OWNER(string)
     Entered BRAND(string)
     Entered WEIGHT(float)
     Entered LENGTH(float)
     Entered LOCATION(string)
     Entered TIMESTAMP(string)
     STATUS(string)
			
DELETE a particular skateboard:
		URL:http://127.0.0.1:8000/skateboard/api/skateboard/<ID>/
		Input: ID of the skateboard should be at the end of the URL. Click on the "DELETE" button to delete the current record.
		
	
	
