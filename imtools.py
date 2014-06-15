#!/usr/bin/env python


import os 

def get_imlist(path):
	"""
	Returns a list of filenames for
	all jpg images in a directory.
	"""

	return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]


if __name__ == "__main__":

	print get_imlist("../images")
