import uuid

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

from backend.models import Purchase
from accounts.models import CustomUser


from django.db.models.query_utils import Q
import random
import string


