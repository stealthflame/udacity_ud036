from __future__ import print_function
import urllib


def read_text():

	a = open("/home/stealthflame/version-control/udacity_ud036/check_profanity/movie_quotes.txt")
	contents_of_file = a.read()
	print(contents_of_file)
	a.close()
	check_profanity(contents_of_file)


def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=shot"+text_to_check)
	result = connection.read()
	
	
	if 'true' in result:
		print("\nProfanity Alert !!!")
	elif "false" in result:
		print("\nThis Document is Clean !!! ")
	else:
		print("\nDocument can't be read !!!")

read_text()