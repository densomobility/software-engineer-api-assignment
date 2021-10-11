from django.test import TestCase, Client
from django.urls import reverse
from skateboard.models import SkateBoard

class TestViews(TestCase):
	
	# this will run before each test method(methods starting with "test")
	def setUp(self):
		self.client = Client()
		self.list_url = reverse("skateboard-list")
		self.detail_url = reverse("skateboard-detail",args=["1"])
		
		self.skateboard1 = SkateBoard.objects.create(
			name_owner="Naruto",
			brand="Baker",
			weight=10,
			length=80,
			location="Michigan",
			timestamp="2021-10-12T00:00:00Z"
		)
		
		self.skateboard2 = SkateBoard.objects.create(
			name_owner="Sasuke",
			brand="Birdhouse",
			weight=15,
			length=85,
			location="West Virginia",
			timestamp="2021-10-10T00:00:00Z"
		)
	

	# Positive testing 
	
	# Get skateboards - GET
	def test_skateboard_list_GET(self):
		response = self.client.get(self.list_url)
		number_of_records_returned = len(response.data)
		
		self.assertEquals(response.status_code,200)
		self.assertEquals(number_of_records_returned,2)
	
	# Create skateboard	- POST
	def test_skateboard_list_POST(self):
		response = self.client.post(self.list_url, {
			"name_owner":"Sakura",
			"brand":"Krooked",
			"weight":5,
			"length":75,
			"location":"California",
			"timestamp":"2021-10-12T00:00:00Z"
		}, content_type="application/json")
		
		number_of_records_in_database = SkateBoard.objects.all().count()
		
		self.assertEquals(response.status_code,201)
		self.assertEquals(number_of_records_in_database,3)
	
	# Get a skateboard - GET
	def test_skateboard_detail_GET(self):
		response = self.client.get(self.detail_url)
		self.assertEquals(response.status_code,200)
		self.assertEquals(response.data["name_owner"],"Naruto")
	
	# Update skateboard - PATCH
	def test_skateboard_detail_PATCH(self):
	
		response = self.client.patch(self.detail_url, {
			"weight":15
		}, content_type="application/json")
		
		self.assertEquals(response.status_code,200)
		self.assertEquals(response.data["weight"],15)
		
	# Delete skateboard - DELETE
	def test_skateboard_detail_DELETE(self):
		response = self.client.delete(self.detail_url)
		number_of_records_in_database = SkateBoard.objects.all().count()
		
		self.assertEquals(response.status_code,204)
		self.assertEquals(number_of_records_in_database,1)
	

	# Check "status" value based on timestamp
	def test_skateboard_detail_PATCH_available_status(self):
	
		response = self.client.patch(self.detail_url, {
			"timestamp":"2019-10-12T00:00:00Z"		# hard-coded 2019 date < 2021. status should be "Available"
		}, content_type="application/json")
		
		self.assertEquals(response.status_code,200)
		self.assertEquals(response.data["status"],"Available")
	
	# Check "status" value based on timestamp
	def test_skateboard_detail_PATCH_not_available_status(self):
	
		url = reverse("skateboard-detail",args=["2"])	
	
		response = self.client.patch(url, {
			"timestamp":"2025-10-12T00:00:00Z"		# hard-coded 2025 date > 2021. status should be "Not Available"
		}, content_type="application/json")
		
		self.assertEquals(response.status_code,200)
		self.assertEquals(response.data["status"],"Not Available")
	
		
	# Negative testing
	
	# check the minimum value of weight
	def test_skateboard_list_POST_weight_less_than_minimum(self):
		response = self.client.post(self.list_url, {
			"name_owner":"Sai",
			"brand":"Krooked",
			"weight":1,	# weight should be >= 2
			"length":75,
			"location":"California",
			"timestamp":"2021-10-12T00:00:00Z"
		}, content_type="application/json")
		
		number_of_records_in_database = SkateBoard.objects.all().count()
		
		self.assertEquals(response.status_code,400)
		self.assertEquals(number_of_records_in_database,2)
	
	# check the maximum value of weight
	def test_skateboard_list_POST_weight_greater_than_maximum(self):
		response = self.client.post(self.list_url, {
			"name_owner":"Sai",
			"brand":"Krooked",
			"weight":21,	# weight should be <= 20
			"length":75,
			"location":"California",
			"timestamp":"2021-10-12T00:00:00Z"
		}, content_type="application/json")
		
		number_of_records_in_database = SkateBoard.objects.all().count()
		
		self.assertEquals(response.status_code,400)
		self.assertEquals(number_of_records_in_database,2)
		
	# check the ID to retrieve a single skateboard	
	def test_skateboard_detail_GET_invaid_ID(self):
		url = reverse("skateboard-detail",args=["100"])		# 100 is not a valid ID. valid IDs are 1 and 2(created only 2 records in the test database)
		response = self.client.get(url)
		self.assertEquals(response.status_code,404)
	
	# check the minimum value of length		
	def test_skateboard_detail_PATCH_length_less_than_minimum(self):
	
		response = self.client.patch(self.detail_url, {
			"length":69		# length should be >= 70
		}, content_type="application/json")
		
		self.assertEquals(response.status_code,400)
		
	# check the maximum value of length
	def test_skateboard_detail_PATCH_length_greater_than_maximum(self):
	
		response = self.client.patch(self.detail_url, {
			"length":91		# length should be <= 90
		}, content_type="application/json")
		
		self.assertEquals(response.status_code,400)
	
	# check the brand		
	def test_skateboard_detail_PATCH_invalid_brand(self):
	
		response = self.client.patch(self.detail_url, {
			"brand":"Bakers"		# brand value should be one among Baker, Birdhouse and Krooked
		}, content_type="application/json")
		
		self.assertEquals(response.status_code,400)
	
	# check the timestamp value	
	def test_skateboard_detail_PATCH_invalid_timestamp(self):
	
		response = self.client.patch(self.detail_url, {
			"timestamp":"2021-10-10T24:00:00Z"		# hours cannot be 24
		}, content_type="application/json")
		
		self.assertEquals(response.status_code,400)
		