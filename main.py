import tweepy
import time
import numpy as np
import pandas as pd
import re
import datetime


CK='JW1Tsn0dh8BOWawfTSxQQC1J8'
CS='62vmqBdu7xj7RZqs6W3FUBcqgNVIjo0LDhGLV8R7lXqKw3lbEF'
AT='1221050313022615552-yAlmTilEHMtYnvtFtN6uTlPrDM8GQ9'
AS='xuKSt9zRORtT2BLKG3i25qWGCff9I0jkflM8vhHI41C3p'

# create twitter object
auth=tweepy.OAuthHandler(CK,CS)
auth.set_access_token(AT,AS)
api=tweepy.API(auth)

api.update_status('first tweet from python\n\nseiya')