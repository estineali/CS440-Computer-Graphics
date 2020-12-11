from myimage import MyImage
import random

#primes
def draw_line_dda(image:'MyImage', P:(int, int), Q:(int, int)):
	default_color = (0, 0, 139, 255) # dark blue

	#Assumption: From left to right, P is the first point, and Q is the second point. 
	if Q[0] < P[0]: #if that assumption is violated, we make it so. 
		P, Q = Q, P

	image.putpixel(P, default_color)
	image.putpixel(Q, default_color)

	#No Line
	if P == Q:
		return True

	#Vertical Line 
	if P[0] == Q[0]: 
		if P[1] > Q[1]:
			P, Q = Q, P
		for i in range(P[1], P[1] + abs(Q[1] - P[1]) + 1):
			image.putpixel((P[0], i), default_color)
		return True
	
	#Horizontal Line
	if P[1] == Q[1]:
		for i in range(P[0], P[0] + abs(Q[0] - P[0]) + 1):
			image.putpixel((i, P[1]), default_color)
		return True
	
	#Sloped Lines
	m = (Q[1] - P[1]) / (Q[0] - P[0]) #gradient
	
	current_pixel = P

	#Q is above P
	if Q[1] < P[1]:
		# X has larger extent
		if 0 < abs(m) <= 1:  
			y_val = current_pixel[1]
			while current_pixel[1] > Q[1]:
				y_val += m #m will be negative here 
				if current_pixel[1] - y_val >= 1: 
					current_pixel = (current_pixel[0] + 1, current_pixel[1] - 1) 
				else:
					current_pixel = (current_pixel[0] + 1, current_pixel[1])
				if current_pixel[0] != Q[0]: #to ensure it doesnt draw a pixel below Q
					image.putpixel(current_pixel, default_color)
			return True

		# Y has larger extent
		elif abs(m) > 1:
			x_val = current_pixel[0]
			while current_pixel[1] > Q[1] + 1:
				x_val -= 1/m #m will be negative here.
				if x_val - current_pixel[0] >= 1: 
					current_pixel = (current_pixel[0] + 1, current_pixel[1] - 1) 
				else:
					current_pixel = (current_pixel[0], current_pixel[1] - 1) 
				if current_pixel[1] != Q[1]: #to ensure it doesnt draw a pixel on the sides of Q
					image.putpixel(current_pixel, default_color)				
			return True
	
	#Q is below P
	elif Q[1] > P[1]: 
		# X has larger extent
		if 0 < m <= 1:
			y_val = current_pixel[1]
			while current_pixel[1] < Q[1]:
				y_val += m
				if abs(y_val - current_pixel[1]) >= 1:
					current_pixel = (current_pixel[0] + 1, current_pixel[1] + 1)
				else:
					current_pixel = (current_pixel[0] + 1, current_pixel[1])
				if current_pixel[0] != Q[0]: #to ensure it doesnt draw a pixel above Q
					image.putpixel(current_pixel, default_color)
			return True

		# Y has larger extent
		elif m > 1: 
			x_val = current_pixel[0]
			while current_pixel[1] < Q[1]:
				x_val += 1/m
				if abs(x_val - current_pixel[0]) >= 1:
					current_pixel = (current_pixel[0] + 1, current_pixel[1] + 1)
				else:
					current_pixel = (current_pixel[0], current_pixel[1] + 1)
				if current_pixel[1] != Q[1]: #to ensure it doesnt draw a pixel to the sides of  Q
					image.putpixel(current_pixel, default_color)
			return True

	return False 

def draw_line(image:'MyImage', P:(int, int), Q:(int, int), color1: (int,)*4, color2: (int,)*4):
	if Q[0] < P[0]:
		P, Q = Q, P
		color1, color2 = color2, color1

	image.putpixel(P, color1)
	image.putpixel(Q, color2)

	#No Line
	if P == Q:
		return [Q] #list will contain only 1 pixel

	pixels = list()

	#Vertical Line 
	if P[0] == Q[0]: 
		if P[1] > Q[1]:
			P, Q = Q, P
			color1, color2 = color2, color1
		for i in range(P[1], P[1] + abs(Q[1] - P[1]) + 1):
			pixels.append((P[0], i))
	
	#Horizontal Line
	elif P[1] == Q[1]:
		for i in range(P[0], P[0] + abs(Q[0] - P[0]) + 1):
			pixels.append((i, P[1]))

	#Sloped Lines
	else:
		m = (Q[1] - P[1]) / (Q[0] - P[0]) #gradient
		
		current_pixel = P

		#Q is above P
		if Q[1] < P[1]:
			# X has larger extent
			if 0 < abs(m) <= 1:  
				y_val = current_pixel[1]
				while current_pixel[1] > Q[1]:
					y_val += m #m will be negative here 
					if current_pixel[1] - y_val >= 1: 
						current_pixel = (current_pixel[0] + 1, current_pixel[1] - 1) 
					else:
						current_pixel = (current_pixel[0] + 1, current_pixel[1])
					if current_pixel[0] != Q[0]: #to ensure it doesnt draw a pixel below Q
						pixels.append(current_pixel)

			# Y has larger extent
			elif abs(m) > 1:
				x_val = current_pixel[0]
				while current_pixel[1] > Q[1] + 1:
					x_val -= 1/m #m will be negative here.
					if x_val - current_pixel[0] >= 1: 
						current_pixel = (current_pixel[0] + 1, current_pixel[1] - 1) 
					else:
						current_pixel = (current_pixel[0], current_pixel[1] - 1) 
					if current_pixel[1] != Q[1]: #to ensure it doesnt draw a pixel on the sides of Q
						pixels.append(current_pixel)			
		
		#Q is below P
		elif Q[1] > P[1]: 
			# X has larger extent
			if 0 < m <= 1:
				y_val = current_pixel[1]
				while current_pixel[1] < Q[1]:
					y_val += m
					if abs(y_val - current_pixel[1]) >= 1:
						current_pixel = (current_pixel[0] + 1, current_pixel[1] + 1)
					else:
						current_pixel = (current_pixel[0] + 1, current_pixel[1])
					if current_pixel[0] != Q[0]: #to ensure it doesnt draw a pixel above Q
						pixels.append(current_pixel)

			# Y has larger extent
			elif m > 1: 
				x_val = current_pixel[0]
				while current_pixel[1] < Q[1]:
					x_val += 1/m
					if abs(x_val - current_pixel[0]) >= 1:
						current_pixel = (current_pixel[0] + 1, current_pixel[1] + 1)
					else:
						current_pixel = (current_pixel[0], current_pixel[1] + 1)
					if current_pixel[1] != Q[1]: #to ensure it doesnt draw a pixel to the sides of  Q
						pixels.append(current_pixel)


		pixels.append(Q) #After all pixels appended, append the final pixel
	# drawing
	colors = interpolate_color(color1, color2, len(pixels))
	for i in range(len(pixels)):
		image.putpixel(pixels[i], colors[i])
		pixels[i] = (pixels[i], colors[i])
	return pixels

def draw_polygon_dda(image:'MyImage', points, colors):
	sides = len(points)

	#If only one pixel then points and colors are not tuples of tuples, but just one individual tuple. Hence: 
	if isinstance(points[0], int) or len(points) == 1: 
		image.putpixel(points, colors)
		return [(points, colors)]
	
	pixels = list()
	
	for i in range(sides):
		pixels += draw_line(image, points[i], points[(i + 1) % sides], colors[i], colors[(i + 1) % sides])
	return pixels 

def draw_polygon(image:'MyImage', points, colors, fill=True):

	#pixels contains the pixel and color pairs for for each line. 
	pixels = draw_polygon_dda(image, points, colors)
	
	if not fill:
		return pixels
	
	row = image.size[1]
	col = image.size[0]

	for y in range(row): #for each row
		
		paint_line = list() #list containing the start and end points of the horizontal line to paint

		for x in range(col): #for each column 
			
			pixel_colored = check_pixel_in_line(pixels, (x, y))
			
			if  pixel_colored != False:
				paint_line.append(pixel_colored)
			
			if len(paint_line) == 2:
				
				p1 = paint_line[0][0]
				p2 = paint_line[1][0]

				color1 = paint_line[0][1]
				
				color2 = paint_line[1][1]

				draw_line(image, p1, p2, color1, color2)
				
				paint_line.clear()

	return pixels

#helpers 
def check_pixel_in_line(pixels, this_pixel):
	for colored_pixel in pixels:
		if this_pixel in colored_pixel:
			return colored_pixel
	return False

def interpolate_color(color1: (int,)*4, color2: (int,)*4, pixels_count:int):
	if pixels_count == 0:
		return color1

	#interpolating between two RGB color values for n (pixels_count) pixels. 
	red_gradient = (color2[0] - color1[0]) / pixels_count
	green_gradient = (color2[1] - color1[1]) / pixels_count
	blue_gradient = (color2[2] - color1[2]) / pixels_count
	alpha_gradient = (color2[3] - color1[3]) / pixels_count

	color_list = list()
	for i in range(pixels_count):
		color_list.append( ( int(color1[0] + red_gradient * i), 
						     int(color1[1] + green_gradient * i), 
						     int(color1[2] + blue_gradient * i), 
						     int(color1[3] + alpha_gradient * i) ) )

	return color_list
	
def get_random_color(): 
	color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255)
	return color

def get_color(color:str):
	colors_mapping = { 'black' : (0, 0, 0, 255),
					   'red' : (255, 0, 0, 255),
					   'green' : (0, 255, 0, 255),
					   'blue' : (0, 0, 255, 255),
					   'white' : (255, 255, 255, 255)
	}
	#add more colors as you need more 

	return colors_mapping[color.strip().lower()]

#tests
def test_draw_line_dda():
	resolution = (20, 10)
	grid_width = 4
	pixel_size = 30; 
	img_mode = 'RGBA'


	# Q is above P, wider extent for X 
	test_img_1 = MyImage(resolution, grid_width, pixel_size, img_mode)
	draw_line_dda(test_img_1, (0, 9), (19, 0))
	test_img_1.show()
	
	# Q is below P, wider extent for X 
	test_img_2 = MyImage(resolution, grid_width, pixel_size, img_mode)
	draw_line_dda(test_img_2, (0, 0), (18, 9))
	test_img_2.show()
	
	# Q is above P, wider extent for Y 
	test_img_3 = MyImage(resolution, grid_width, pixel_size, img_mode)
	draw_line_dda(test_img_3, (0, 9), (7, 0))
	test_img_3.show()
	
	# Q is below P, wider extent for Y 
	test_img_4 = MyImage(resolution, grid_width, pixel_size, img_mode)
	draw_line_dda(test_img_4, (0, 0), (8, 9))
	test_img_4.show()

	#testign all horizontal lines are drawing. There should not be a single empty box.
	test_hori_lines = MyImage(resolution, grid_width, pixel_size, img_mode)
	for i in range(0, resolution[1]):
		draw_line_dda(test_hori_lines, (0, i), (resolution[0] - 1, i))
	test_hori_lines.show()

	#testing all vertical lines are drawing. There should not be a single empty box. 
	test_vert_lines = MyImage(resolution, grid_width, pixel_size, img_mode)
	for j in range(0, resolution[0]):
		draw_line_dda(test_vert_lines, (j, 0), (j, resolution[1] - 1))
	test_vert_lines.show()

def test_draw_line():
	resolution = (20, 10)
	grid_width = 4
	pixel_size = 30; 
	img_mode = 'RGBA'

	# Q is above P, wider extent for X 
	test_img_1 = MyImage(resolution, grid_width, pixel_size, img_mode)
	draw_line(test_img_1, (0, 9), (19, 0), get_random_color(), get_random_color())
	test_img_1.show()
	
	# Q is below P, wider extent for X 
	test_img_2 = MyImage(resolution, grid_width, pixel_size, img_mode)
	draw_line(test_img_2, (0, 0), (18, 9), get_random_color(), get_random_color())
	test_img_2.show()
	
	# Q is above P, wider extent for Y 
	test_img_3 = MyImage(resolution, grid_width, pixel_size, img_mode)
	draw_line(test_img_3, (0, 9), (7, 0), get_random_color(), get_random_color())
	test_img_3.show()
	
	# Q is below P, wider extent for Y 
	test_img_4 = MyImage(resolution, grid_width, pixel_size, img_mode)
	draw_line(test_img_4, (0, 0), (8, 9), get_random_color(), get_random_color())
	test_img_4.show()

	#testign all horizontal lines are drawing. There should not be a single empty box.
	test_hori_lines = MyImage(resolution, grid_width, pixel_size, img_mode)
	for i in range(0, resolution[1]):
		draw_line(test_hori_lines, (0, i), (resolution[0] - 1, i), get_random_color(), get_random_color())
	test_hori_lines.show()

	#testing all vertical lines are drawing. There should not be a single empty box. 
	test_vert_lines = MyImage(resolution, grid_width, pixel_size, img_mode)
	for j in range(0, resolution[0]):
		draw_line(test_vert_lines, (j, 0), (j, resolution[1] - 1), get_random_color(), get_random_color())
	test_vert_lines.show()


	return True 

def test_draw_polygon_dda():
	resolution = (19, 10)
	grid_width = 4
	pixel_size = 30; 
	img_mode = 'RGBA'

	test_img_0 = MyImage(resolution, grid_width, pixel_size, img_mode)
	draw_polygon_dda(test_img_0, ((8, 4)), (get_random_color()))
	test_img_0.show()

	test_img_1 = MyImage(resolution, grid_width, pixel_size, img_mode)
	draw_polygon_dda(test_img_1, ((1, 8), (10, 0), (18, 4)), ((get_random_color(), get_random_color(), get_random_color())))
	test_img_1.show()

	test_img_2 = MyImage(resolution, grid_width, pixel_size, img_mode)
	draw_polygon_dda(test_img_2, ((0, 0), (18, 0), (18, 9), (0, 9)), ((get_random_color(), get_random_color(), get_random_color(), get_random_color())))
	test_img_2.show()

	test_img_3 = MyImage(resolution, grid_width, pixel_size, img_mode)
	draw_polygon_dda(test_img_3, ((1, 1), (18, 1), (18, 8), (1, 8)), (((255, 0, 0, 255), (0, 255, 0, 255), (0, 0, 255, 255), (255, 255, 255, 255))))
	test_img_3.show()

	test_img_4 = MyImage(resolution, grid_width, pixel_size, img_mode)
	draw_polygon_dda(test_img_4, ((1, 8), (9, 1), (18, 8)), ((get_random_color(), get_random_color(), get_random_color())))
	test_img_4.show()

	return True

def test_draw_polygon():
	resolution = (25, 15)
	grid_width = 4
	pixel_size = 30 
	img_mode = 'RGBA'

	# single point
	test_img_0 = MyImage(resolution, grid_width, pixel_size, img_mode)
	points_img_0 = ((8, 4))
	colors_img_0 = (get_random_color())
	draw_polygon(test_img_0, points_img_0, colors_img_0)
	test_img_0.show()

	#random colors triangle 1
	test_img_1 = MyImage(resolution, grid_width, pixel_size, img_mode)
	points_img_1 = ((1, 8), (10, 0), (18, 4))
	colors_img_1 = (get_random_color(), get_random_color(), get_random_color())
	draw_polygon(test_img_1, points_img_1, colors_img_1)
	test_img_1.show()

	#random colors rectangle
	test_img_2 = MyImage(resolution, grid_width, pixel_size, img_mode)
	points_img_2 = ((0, 0), (18, 0), (18, 9), (0, 9))
	colors_img_2 = (get_random_color(), get_random_color(), get_random_color(), get_random_color())
	draw_polygon(test_img_2, points_img_2, colors_img_2)
	test_img_2.show()

	#RGB rectangle
	test_img_3 = MyImage(resolution, grid_width, pixel_size, img_mode)
	points_img_3 = ((1, 1), (18, 1), (18, 8), (1, 8))
	colors_img_3 = (get_color('green'), get_color('blue'), get_color('white'), get_color('red'))
	draw_polygon(test_img_3, points_img_3, colors_img_3)
	test_img_3.show()

	#random colors triangle 2
	test_img_4 = MyImage(resolution, grid_width, pixel_size, img_mode)
	points_img_4 = ((1, 8), (9, 1), (18, 8))
	colors_img_4 = (get_random_color(), get_random_color(), get_random_color())
	draw_polygon(test_img_4, points_img_4, colors_img_4)
	test_img_4.show()

	#two points
	test_img_5 = MyImage(resolution, grid_width, pixel_size, img_mode)
	points_img_5 = ((1, 8), (9, 1))
	colors_img_5 = (get_random_color(), get_random_color())
	draw_polygon(test_img_5, points_img_5, colors_img_5)
	test_img_5.show()

	#random red_black rectangle
	test_img_6 = MyImage(resolution, grid_width, pixel_size, img_mode)
	points_img_6 = ((0, 0), (18, 0), (18, 9), (0, 9))
	colors_img_6 = (get_color('black'), get_color('black'), get_color('black'), get_color('red'))
	draw_polygon(test_img_6, points_img_6, colors_img_6)
	test_img_6.show()

	#random green_black rectangle
	test_img_7 = MyImage(resolution, grid_width, pixel_size, img_mode)
	points_img_7 = ((0, 0), (18, 0), (18, 9), (0, 9))
	colors_img_7 = (get_color('black'), get_color('green'), get_color('black'), get_color('black'))
	draw_polygon(test_img_7, points_img_7, colors_img_7)
	test_img_7.show()


	return True


if __name__ == '__main__':
	# test_draw_line_dda()
	# test_draw_line()
	# test_draw_polygon_dda()
	test_draw_polygon()
