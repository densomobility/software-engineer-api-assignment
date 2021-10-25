# software-engineer-api-assignment
## Instructions to run locally:
1. Clone respository 
```git clone https://github.com/wmati/software-engineer-api-assignment```
2. Create Python virtual environment at downloaded location. Note: At this point you should be in the same directory as manage.py
```python -m venv env```
3. Activate virtual environment
```env\scripts\activate```
4. Install Django and Django REST Framework (DRF) with Pip
```
pip install django
pip install djangorestframework
```
5. Create SQL Lite Database
```python manage.py migrate```
6. Run Server
```python manage.py runserver```
7. The command line will indicate the port the app is launched.
```Starting development server at http://127.0.0.1:8000/```
8. To run unit test:
```python manage.py test```

## Considerations for Future Improvement
1. Address case sensitivity in URL
2. Filter by skateboard type, spec, brand
3. Improved JSON formatting

## Completed Stories
<b>As a skateboard owner I want to be able to add my individual board to a skateboard sharing marketplace.</b>
1. Go to 127.0.0.1:8000
2. Insert your data in JSON fromat, or paste provided data (below) and press POST
```
{
            "available" : 1,
            "owner": "John",
            "brand": "Element",
            "weight": 5,
            "length": 30,
            "type": "skateboard",
            "city": "Buffalo",
            "state": "NY"
}
```
3. Refresh page, and a GET request will automatically be submitted. The new posting should be visible.

<b>As a skateboard owner I want to be able to modify the details for the board that I share.</b>
1. Go to 127.0.0.1:8000/user/*your name*/*posting ID*  (for example if your posting name is John and you already have a posting with ID=1, go to 127.0.0.1:8000/user/John/1)
2. Re-enter data to be updated in JSON format. Note, not all fields need to be entered. For example, input of the following will be sufficient:
```
{
            "available" : 1,
            "brand": "West 49",
}
```
3. Refresh page, or go to homepage to see listing

<b>As a skateboard owner I want to be able to indicate that my board is available or unavailable for sharing</b><br/>
This story is satisfied by the *available* parameter in the object, which is specified by a boolean. 1 represents AVAILABLE and 0 represents UNAVAILABLE.
Changing the status is submitted by a PUT request as explained in the previous story.

<b>As a skateboard borrower, I want to see a list of available boards</b><br/>

Go to 127.0.0.1:8000/available/*boolean* <br/>
-AVAILABLE BOARDS: 127.0.0.1:8000/available/1<br/>
-UNAVAILABLE BOARDS: 127.0.0.1:8000/available/0

**Skateboards by User**
1. Go to 127.0.0.1:8000/user/*your name* (ex 127.0.0.1:8000/users/John)

**Delete Board**
1. Go to 127.0.0.1:8000/user/*your name*/*posting ID*
2. Press DELETE or submit a delete request
            
## Summary

| Endpoint | HTTP Verbs | Screenshot |
| --- | --- | --- |
| 127.0.0.1:8000 | GET, POST | ![Capture](https://user-images.githubusercontent.com/14862636/138574907-c4c0ebaf-3c24-4449-9853-0f83cc5007dc.JPG) |
| 127.0.0.1:8000/available/*boolean*/ | GET | ![Capture](https://user-images.githubusercontent.com/14862636/138574917-406165fd-e173-4a2c-ac93-775e0ddabdca.JPG) |
| 127.0.0.1:8000/user/*username*/*posting id*/ | GET, PUT, DELETE | ![Capture](https://user-images.githubusercontent.com/14862636/138575014-74434c45-cfdb-4e19-beb2-00236f11cfad.JPG) |
| 127.0.0.1:8000/user/*username*/| GET | ![image](https://user-images.githubusercontent.com/14862636/138575445-3a2df3f0-71c1-4fa1-ac30-1fa87bd095d2.png) |
