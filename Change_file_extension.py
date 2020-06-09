import os

directory = '/Users/Alex/Desktop/Bubble_Images/test#7 20ppm MIBC'
for filename in os.listdir(directory):
    if filename.endswith('.bmp'):
        base = os.path.splitext(filename)[0]
        os.rename(directory + '/' + filename, directory + '/' + base + '.jpg')
        continue
    else:
        continue
