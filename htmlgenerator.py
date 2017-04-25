#Based on the design (design.html and the stylesheet) build a generator for the HTML file
#This will make changes and editing a lot easier and more flexible given the quantitiy of entries

#create a variable that loops the content by weeks
content = "Testing"


#create a list with the html design, line by line
base = [
	'<!DOCTYPE html>',
	'<html>',
	'<head>',
		'<title>One Hundered and Six Weeks</title>',
		'<link rel="stylesheet" type="text/css" href="stylesheet.css">',
		'<link href="https://fonts.googleapis.com/css?family=Open+Sans+Condensed:300" rel="stylesheet">',
	'</head>',
	'<body>',
	'	<div class="intro">',
	'		<div class="introspacer"></div>',
	'		<h1>One Hunderd and Six Memories</h1>',
	'		<h4>from</h4>',
	'		<h1>One Hunderd and Six Weeks</h1>',
	'	</div>',
	content,
	'</body>',
	'</html>'

]

#open a new file which will be the html file, and 
with open ("index.html", "w") as fo:
	for line in base:
		fo.write(line + '\n')

	# for link in links:
	# 	fo.write(link.encode('utf-8')+'</br>'+'</br>') 