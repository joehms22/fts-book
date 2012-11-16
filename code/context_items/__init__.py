#!/usr/bin/env python3
'''
The context item class, essentially just calls others to get the job done.
'''

import context_items.calculator
import context_items.easter_eggs


ENABLED_CONTEXT_ITEMS = [calculator, easter_eggs]

def generate_context(query, doc_id_rank_map, database):
	
	output = ""
	
	for item in ENABLED_CONTEXT_ITEMS:
		html = item.get_item(query, doc_id_rank_map, database)
	
	
		if not html == None and len(html) != 0:
			output += "<article>"
			if item.TITLE != None and len(item.TITLE) != 0:
				output += "<h2>%s</h2>" % (item.TITLE)
			output += "%s" % (html)
			output += "</article>"

	return output
