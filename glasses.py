#!/usr/bin/python


from image_parser import ImageDealer

id = ImageDealer()

filename = 'leo_r.jpg'
predict = id.parse_image(filename)
print("Shape of face is {}".format(predict))