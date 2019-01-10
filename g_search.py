#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pedro Gabaldon

import urllib2
import re
 
from googleapiclient.discovery import build

from colors import *

API_KEY = ''
CX = ''

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Connection': 'close'}

def search(q, opts, out_queue=None):
	service = build('customsearch', 'v1', developerKey=API_KEY)

	res = service.cse().list(q=q, cx=CX).execute()

	points(res, q, opts)

def points(response, q, opts, color=bcolors.OKBLUE):
	for i in response['items']:
		req = urllib2.Request(i['link'], headers=hdr)
		try:
			content = urllib2.urlopen(req).read().lower()
		except (urllib2.HTTPError, urllib2.URLError):
			continue	
		
		p = [0, 0, 0] # Points
		p[0] += len(re.findall(opts[0], content))
		p[1] += len(re.findall(opts[1], content))
		p[2] += len(re.findall(opts[2], content))

		for w in opts[0].split():
			p[0] += 0.5*len(re.findall(w, content))

		for w in opts[1].split():
			p[1] += 0.5*len(re.findall(w, content))

		for w in opts[2].split():
			p[2] += 0.5*len(re.findall(w, content))
				
		print opts[0] + ': ' + bcolors.OKGREEN + bcolors.BOLD + str(p[0]) + bcolors.ENDC
		print opts[1] + ': ' + bcolors.OKGREEN + bcolors.BOLD + str(p[1]) + bcolors.ENDC
		print opts[2] + ': ' + bcolors.OKGREEN + bcolors.BOLD + str(p[2]) + bcolors.ENDC
		iM = p.index(max(p))

		if 'NO' in q:
			iM = p.index(min(p))

		print 'Best option: ' + color + bcolors.BOLD + str(iM + 1) + bcolors.ENDC
		print '\n'	

	''' res = service.cse().list(q=q, cx=CX, start=11).execute()

	for i in res['items']:
		req = urllib2.Request(i['link'], headers=hdr)
		try:
			content = urllib2.urlopen(req).read()
		except urllib2.HTTPError:
			continue

		p = []
		p.append(len(re.findall(opts[0], content)))
		p.append(len(re.findall(opts[1], content)))
		p.append(len(re.findall(opts[2], content)))
				
		print opts[0] + ': ' + str(p[0])
		print opts[1] + ': ' + str(p[1])
		print opts[2] + ': ' + str(p[2])
		iM = p.index(max(p))
		print 'Best option: ' + bcolors.OKGREEN + str(iM + 1) + bcolors.ENDC
		print '\n' '''


