from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets
from django_filters import rest_framework as filters
import datetime
import pytz

from .models import SkateBoard
from .serializers import SkateBoardSerializer




# filters the database 
class SkateBoardFilter(filters.FilterSet):
	
	# valid values for filtering the "timestamp" column
	STATUS_CHOICES = (
		('Available', 'Available'),
		('Not Available', 'Not Available'),
	)

	weight_lte = filters.NumberFilter(field_name="weight",lookup_expr="lte")	
	weight_gte = filters.NumberFilter(field_name="weight",lookup_expr="gte")
	length_lte = filters.NumberFilter(field_name="length",lookup_expr="lte")	
	length_gte = filters.NumberFilter(field_name="length",lookup_expr="gte")
	status = filters.ChoiceFilter(label="Status",field_name="timestamp", method='check_status',choices=STATUS_CHOICES)
	
	# filtering the "timestamp" column based on the STATUS_CHOICES values
	def check_status(self, queryset, name, value):
		if value == 'Available':
			return queryset.filter(timestamp__lte=datetime.datetime.now(pytz.utc))
		elif value == 'Not Available':
			return queryset.filter(timestamp__gt=datetime.datetime.now(pytz.utc))
		
	class Meta:
		# filtering against the SkateBoard database table records
		model = SkateBoard
		# columns that can be filtered
		fields = ('id', 'name_owner', 'brand', 'weight', 'length', 'location', 'status', 'weight_lte', 'weight_gte', 'length_lte', 'length_gte')

	
	
class SkateBoardViewSet(viewsets.ModelViewSet):
	# This viewset automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions
	
	queryset = SkateBoard.objects.all()			# database table records
	serializer_class = SkateBoardSerializer		# serializer for serializing, de-serializing and validation
	filter_class = SkateBoardFilter				# filter class
	
			
				
