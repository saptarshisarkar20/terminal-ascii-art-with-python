from pywhatkit import image_to_ascii_art
image = "img.jpg"
text = "abcd.txt"
image_to_ascii_art(image, text)
file1 = open(text,"r")
while(True):
	#read next line
	line = file1.readline()
	#check if line is not null
	if not line:
		break
	#you can access the line
	print(line.strip())

#close file
file1.close