#!/usr/bin/env python3
'''
When given a list of documents, finds common metadata that is common amongst
them, and gives links back.

'''





TITLE = ""


UNIVERSE = ["life","universe","everything"]
BARREL_ROLL = ['barrel','roll']
RICKROLL = ['the','game']

def all_words_in_query(word_list, query):
	for word in word_list:
		if word not in query:
			return False
	
	return True


def get_item(query, doc_id_rank_map, database):
	''' Checks to see if the user asked for the ultimate answer.
	'''
			
	if all_words_in_query(BARREL_ROLL, query):
		return """<script type='text/javascript'>window.onload=function(){var s=document.createElement('style');s.innerHTML='%40-moz-keyframes roll { 100%25 { -moz-transform: rotate(360deg); } } %40-o-keyframes roll { 100%25 { -o-transform: rotate(360deg); } } %40-webkit-keyframes roll { 100%25 { -webkit-transform: rotate(360deg); } } body{ -moz-animation-name: roll; -moz-animation-duration: 4s; -moz-animation-iteration-count: 1; -o-animation-name: roll; -o-animation-duration: 4s; -o-animation-iteration-count: 1; -webkit-animation-name: roll; -webkit-animation-duration: 4s; -webkit-animation-iteration-count: 1; }';document.getElementsByTagName('head')[0].appendChild(s);}());</script>"""
	
	
	words = 0
	for word in RICKROLL:
		if word in query:
			words += 1
	
	if all_words_in_query(RICKROLL, query):
		return """<h2>You Just Lost The Game<h2><iframe width="420" height="315" src="http://www.youtube.com/embed/oHg5SJYRHA0?autoplay=1" frameborder="0" allowfullscreen></iframe>"""
	
	if all_words_in_query(UNIVERSE, query):
		return """<h2>The answer to life the universe and everything: 42</h2>"""
