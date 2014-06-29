#
# spotify_api.py
# Lema Kikuchi
# June 23, 2014
#
# https://developer.spotify.com/technologies/metadata-api/search/
#

from urllib2 import urlopen
import urllib
from xml.etree import cElementTree as ET
import re
import string
import time

import code

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pickle


from bs4 import BeautifulSoup


#constants#####################################
#pieces of the spotify API URL
SPOTIFY_SEARCH_BASE = 'http://ws.spotify.com/search/1/track?q='
URL_PAGE = '&page='

#if search API finds at least one track, response string length should be greater than this
MIN_RESPONSE_LEN = 500



#functions#####################################
def make_search_url(word, page_num):
	return SPOTIFY_SEARCH_BASE + word + URL_PAGE + str(page_num)

def get_track_page(word,page_num):
	search_url = make_search_url(word, page_num)
	# get the response from search API
	spotify_response = urlopen(search_url)
	#if code is not 200, no good.. no error handling for now return and get out
	if spotify_response.getcode() != 200:
		return 0
	#read into string
	response_string = spotify_response.read()
	#if the string is short than no results were found, so return 0
	if len(response_string) < MIN_RESPONSE_LEN:
		return 0
	#return the response string
	return response_string



words = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']


for word in words:
	page_num = 1
	df = pd.DataFrame(columns=['name','popularity','length'])

	while True:
		response_string = get_track_page(word,page_num)
		if response_string == 0:
			print 'breaking at page ', page_num
			break

		soup = BeautifulSoup(response_string)
		tracks = soup.find_all('track')

		df_temp = pd.DataFrame(columns=['name','popularity','length'])
		df_temp['name'] = [track.find('name') for track in tracks]
		df_temp['popularity'] = [track.find('popularity') for track in tracks]
		df_temp['length'] = [track.find('length') for track in tracks]

		df_temp = df_temp.dropna()
		df = pd.concat([df, df_temp], ignore_index=True)

		page_num += 1
		# print page_num

	df['name'] = [name.string for name in df['name']]
	df['popularity'] = [float(name.string) for name in df['popularity']]
	df['length'] = [float(name.string) for name in df['length']]

	print 'popularity and length of songs about ' + word
	print df[['popularity','length']].describe()

	df.to_pickle(word)

	zeros = df.popularity==0
	df.popularity[zeros] = np.nan
	df.length[zeros] = np.nan

	zero_len = df.length==0
	df.popularity[zero_len] = np.nan
	df.length[zero_len] = np.nan

	print 'popularity and length of songs about ' + word + ' after removing zeros'
	print df[['popularity','length']].describe()






#df to csv
#df to pickle 	
#matplotlib http://matplotlib.org/api/axes_api.html





