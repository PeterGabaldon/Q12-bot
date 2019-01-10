#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pedro Gabaldon

from googleapiclient.discovery import build

from g_search import *


def gNLP(q, opts):
	body = {'document' : {'type' : 'PLAIN_TEXT', 'language' : 'es', 'content' : q}, 'encoding_type' : 'UTF32'}
	qkW = ''
	wURLS = []

	serviceNLP = build('language', 'v1')
	serviceCS = build('customsearch', 'v1', developerKey=API_KEY)

	responseNLP = serviceNLP.documents().analyzeEntities(body=body).execute()

	for kW in responseNLP['entities']:
		qkW += kW['mentions'][0]['text']['content'] + ' '
		if 'wikipedia_url' in kW['metadata']:
			wURLS.append(kW['metadata']['wikipedia_url'])
	qkW = qkW.lower()
	print '\nKey words: ' + qkW + '\n'
	print 'Wikipedia: ' + str(wURLS) + '\n'

	responseCS = serviceCS.cse().list(q=qkW, cx=CX).execute()

	if wURLS:
		points(wURLS, q, opts, color=bcolors.FAIL)	

	points(responseCS, q, opts, color=bcolors.FAIL)
				

