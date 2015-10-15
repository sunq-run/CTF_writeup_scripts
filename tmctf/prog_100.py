#!/usr/bin/python

import mechanize
import wget 
from PIL import Image
x = 0
y = 0
def kaiseki(image):
	img = Image.open(image)
	img.convert("RGB")

	pixelSizeTuple = img.size

	rlist = []
	glist = []
	blist = []
	hikaku = 0

	for i in range(pixelSizeTuple[0]):
		for j in range(pixelSizeTuple[1]):
			r,g,b = img.getpixel((i,j))
			sum = r + g + b
			if sum == 765:
		                continue
	                else:
				if sum > hikaku:
					hikaku = sum
					x = i
					y = j
				else:
				 	continue
        print "\n"
	print "click!" + " " + str(x) + " " + str(y)
	return [x,y]


url = "http://ctfquest.trendmicro.co.jp:43210/click_on_the_different_color"
br = mechanize.Browser()
br.set_handle_robots( False )
res = br.open(url)

while 1:
	a = res.read()
	print a
	image_url = a.split("\"")
	image_url = "http://ctfquest.trendmicro.co.jp:43210" + image_url[3]
	print image_url
	image_name = image_url.split("/")[4]
	print image_url.split("/")[4]
	wget.download(image_url)
	x,y = kaiseki(image_name)
	submit_url = "http://ctfquest.trendmicro.co.jp:43210/" + image_name.split(".")[0] + "?x=" + str(x) + "&y=" + str(y)
	print submit_url
	res = br.open(submit_url)
