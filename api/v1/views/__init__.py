#!/usr/bin/python3
""" views init """

from flask import Blueprint


url_prefix = "/api/v1"

app_views = Blueprint("app_views", __name__, url_prefix=url_prefix)

from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
from api.v1.views.places import *
from api.v1.views.places_reviews import *
from api.v1.views.places_amenities import *
