#Based on the design (design.html and the stylesheet) build a generator for the HTML file
#This will make changes and editing a lot easier and more flexible given the quantitiy of entries

import csv
#itertools to merge lists
import itertools 

# import the content file as a list which is formatted as date, week, content such as image, title, paragraph
content = []
# NOTE currently using with test csv
with open('contenttest.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, dialect=csv.excel_tab, delimiter = ',')
	for row in spamreader:
		content.append([row[0],row[1],row[2],row[3],row[4]])

#format the content into the html format required
formattedcontent = []

index = 0
for entry in content:
	index += 1
	weekhtml = [
		'<div class="textboxA">',
		'	<div class="headerspacertop"></div>',
		'	<div class="topheader">',
		'		<h2>'+entry[1]+'</h2>',
		'		<div class="thickline"></div>',
		'	</div>',
		'	<div class="headerspacerbottom"></div>',
		'	<div class="content">',
		'		<img src="'+entry[2]+'" alt="Week 1 image" class="screenshot">',
		'	</div>',
		'	<div class="captionbox">',
		'		<h3>'+entry[3]+'</h3>',
		'		<div class="thinline"></div>',
		'		<p>'+entry[4]+'</p>',
		'	</div>',
		'</div>'
	]
	formattedcontent.append(weekhtml)

#create a big chunk of code that has all the formatted entries together in one variable
allentries = list(itertools.chain(*formattedcontent))

# print allentries

#create a list with the html design, line by line
base = [
	'<!DOCTYPE html>',
	'<html>',
	'<head>',
		'<title>One Hundred and Five Weeks</title>',
		'<link rel="stylesheet" type="text/css" href="stylesheet.css">',
		'<link href="https://fonts.googleapis.com/css?family=Open+Sans+Condensed:300" rel="stylesheet">',
	'</head>',
	'<body>',
	'	<div class="intro">',
	'		<div class="introspacer"></div>',
	'		<h1>One Hundred and Five Memories</h1>',
	'		<h4>from</h4>',
	'		<h1>One Hundred and Five Weeks</h1>',
	'	</div>',
	str(allentries),
	'</body>',
	'</html>'

]

#open a new file which will be the html file, and 
with open ("index.html", "w") as fo:
	for line in base:
		fo.write(line + '\n')