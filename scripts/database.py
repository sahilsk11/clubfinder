#!/usr/bin/python

print "Content-type: application/json\n\n"

import shelve
import json
import cgi

def new_club(name, categories, description, school, f):
    g = {"name":name, "categories":categories, "description":description}
    f[school].append(g)
    return g

clubs = shelve.open("information_data.shelve", writeback=True)
if not ("clubs" in clubs):
    clubs = {"harker":[], "users":{"unique":0}}
    
form = cgi.FieldStorage()
command = form.getfirst("command", "")
school = form.getfirst("school", "")
clubs["harker"] = []
clubs["harker"].append(new_club("Red Cross", ["humanitarian"], "Red Cross aims to help others everywhere."))
if (command == "pageload"):
    d = clubs[school]
    j = json.dumps(d)
    print j