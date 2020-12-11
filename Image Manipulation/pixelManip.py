from myimage import MyImage
import random

path = r".\images\logo.png"

#Q2 Blow it up
def blow(path):

	grid_lines_width = 1
	pixel_size = 2
	img_default = MyImage.open(path)

	img_default_blown = MyImage(img_default.size, grid_lines_width, pixel_size)
	img_default_blown.putdata(img_default.getdata())
	img_default_blown.show()

	img_red = MyImage(img_default.size, grid_lines_width, pixel_size)
	#taking pixel information from default image
	#and putting only red component of each pixel
	img_red.putdata([(i[0], 0, 0, i[3]) for i in img_default.getdata()])
	img_red.show()

	img_green = MyImage(img_default.size, grid_lines_width, pixel_size)
	#taking pixel information from default image
	#and putting only green component of each pixel
	img_green.putdata([(0, i[1], 0, i[3]) for i in img_default.getdata()])
	img_green.show()

	img_blue = MyImage(img_default.size, grid_lines_width, pixel_size)	
	#taking pixel information from default image
	#and putting only blue component of each pixel
	img_blue.putdata([(0, 0, i[2], i[3]) for i in img_default.getdata()])
	img_blue.show()

	img_cmyk = MyImage(img_default.size, grid_lines_width, pixel_size, 'CMYK')
	#taking pixel information from default image
	#and converting alpha values into black values 
	img_cmyk.putdata([(i[0], i[1], i[2], 255 - i[3]) for i in img_default.getdata()])
	img_cmyk.show()
