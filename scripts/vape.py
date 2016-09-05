from PIL import Image

im = Image.open("vape.png")
out = Image.new('RGB', (im.size[0], im.size[1]))
for i in range(im.size[0]):
	for j in range(im.size[1]):
		if (im.getpixel((i, j))[1] % 2) == 1:
			out.putpixel((i, j), (0, 0, 0))
		else:
			out.putpixel((i, j), (255, 255, 255))

out.save("v.png")
