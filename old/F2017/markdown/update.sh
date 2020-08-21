#!/bin/bash

here="$(dirname "$(readlink -m "$0")")/"
target="$HOME/public_html/2910/F2017/"

htmlheader='﻿<!DOCTYPE html>
<html>
<head>
	<title>CS 2910: Teaching Assistant Practicum</title>
	<link rel="stylesheet" href="stylesheet.css">
</head>
<body>'

function getheader() {
	perl Markdown.pl "$1" | grep '<h1>' | head -1
}
function tagstrip() {
	echo "$1" | sed -e 's~^\(<[^>]*>\)*~~g' -e 's~\(<[^>]*>\)*$~~g'
}

function update() {
	f="$1"
	name="$2"

	echo "$htmlheader"
	getheader "$f" | sed -e 's/<h1>/<h1 class="top">CS 2910: /'
	echo '<div class="menu">'
	last="!";
	for g in *.md
	do
		if [ "$f" != "$g" ]
		then
			gname="${g%.md}"
			
#			if [ "$last" '<' "notes" ] && [ "$gname" '>' "notes" ] 
#			then
#				echo '	<a href="notes.php">Notes</a>'
#			fi
			last="$gname"
			
			ghead="$(getheader "$g" | egrep -v '>[^>]*[0-9]:')"
			if [ -n "$ghead" ]
			then
				echo '	<a href="'"$gname.html"'">'$(tagstrip "$ghead")'</a>'
			fi
		fi
	done
	echo '</div>'
	echo '<blockquote style="background-color:#fbb; font-size:150%">This page does not represent <a href="../">the most current semester</a> of this course; it is present merely as an archive.</blockquote>';
	pandoc "$f" --smart --from=markdown_mmd+link_attributes | tail -n +2 | sed -e 's!p>&lt;\(form .*\)&gt;</p!\1!g' \
		-e 's!\(<.*\)&quot;\(.*\)&quot;\(.*>\)!\1"\2"\3!g' \
		-e 's!\(<.*\)&quot;\(.*\)&quot;\(.*>\)!\1"\2"\3!g' \
		-e 's!\(<.*\)&quot;\(.*\)&quot;\(.*>\)!\1"\2"\3!g' \
		-e 's!\(<.*\)&quot;\(.*\)&quot;\(.*>\)!\1"\2"\3!g'
	echo -n '<center class="bottom">Copyright © '
	date +%Y
	echo ' by Luther Tychonievich. All rights reserved.'
	echo -n '	<br/>Last updated '﻿
	stat -c %y "$f" | sed -e 's/:\([0-9][0-9]\):[\.0-9]*/:\1/g'
	echo '</center>'
	echo '</body>'
	echo '</html>'
}

cd "$here"
for f in *.md
do
	name="${f%.md}"
	if [ "$f" -nt "$target$name.html" ] || [ -n "$1" ]
	then
		echo 'updating' "$target$name.html"
		update "$f" "$name" > "$target$name.html"
	fi
done

for f in *.{png,svg,jpg,tar,txt,c,h,s,ys,yo,pdf,gnuplot,hcl,zip,d,css}
do
	if [ "$f" -nt "$target$f" ]
	then
		echo 'copying' "$f"
		cp "$f" "$target";
	fi
done

exit 0

tail -n +$(grep -n '<table' schedule.md | cut -d':' -f1) schedule.md | sed -e 's/\&/&amp;/g' > /tmp/cal.xml
xmllint --xpath '//td[not(@*)]/a/..' /tmp/cal.xml | python -c '
import sys
date = ""
links = []
for line in sys.stdin:
	if "\"date\">" in line:
		if links: 
			with open("'$target'notes/.htlinks/"+date+".lnk", "w") as f:
				print >> f, "<br/>".join(links)
		date = line[line.find(">")+1:line.rfind("<")]
		links = []
	if "href=" in line:
		links.append(line[line.find("<a"):line.rfind("</a>")+4])
if links: 
	with open("'$target'notes/.htlinks/"+date+".lnk", "w") as f:
		print >> f, "<br/>".join(links)
'
