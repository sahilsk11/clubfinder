#!/usr/bin/python

print "Content-type: application/json\n\n"

import shelve
import json
import cgi
from operator import itemgetter

def new_club(name, categories, description):
    g = {"name":name, "categories":categories, "description":description}
    return g

clubs = shelve.open("information_data.shelve", writeback=True)
users = shelve.open("user_data.shelve", writeback=True)
if not ("unique" in users):
    users["unique"] = {}
    users["total"] = 0
if not ("schools" in clubs):
    clubs["schools"] = {"harker":[]}
    
form = cgi.FieldStorage()
command = form.getfirst("command", "")
school = form.getfirst("school", "")
name = form.getfirst("name", "")
description = form.getfirst("description", "")
categories = form.getfirst("categories", "")
user = form.getfirst("user", "")

if (command == "pageload"):
    categories = categories.split(",")
    clubs_arr = clubs["schools"][school]
    d = []
    if (len(categories) == 0):
        d = clubs_arr
    else:
        for club in clubs_arr:
            all_there = True
            for category in categories:
                if not (category in club["categories"]):
                    all_there = False
            if (all_there):
                d.append(club)
    j = json.dumps(d)
    print j
    
if (command == "newclub"):
    if (not school in clubs["schools"]):
        clubs["schools"][school] = []
    clubs["schools"][school].append(new_club(name, categories, description))
    clubs["schools"][school] = sorted(clubs["school"][school])
    clubs["schools"][school] = sorted(clubs["schools"][school], key=itemgetter('name')) 
    d = {"sucess":True}
    j = json.dumps(d)
    print j

if (command == "user_set"):
    users["unique"][user] = 0
    d = user
    j = json.dumps(d)
    print j

clubs.close()