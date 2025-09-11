import imageio.v3 as iio
import os

filenames = ['team-pic1.png', 'team-pic2.png']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('team.gif', images, duration=500, loop=0)

# Confirmation message
print("GIF created successfully:", os.path.abspath("team.gif"))
