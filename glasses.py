#!/usr/bin/python


from src.image_parser import ImageDealer

id = ImageDealer()

filename = 'anc.jpg'
predict = id.parse_image(filename)
print("Shape of face is {}".format(predict))