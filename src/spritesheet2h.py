#!/usr/bin/env python
import Image
import pprint
import sys

if len(sys.argv) < 2:
    print "./spritesheet2h.py <spritesheet_file>"

pp = pprint.PrettyPrinter(indent=4)

im = Image.open(sys.argv[1])

# get the palette of the sprite sheet, ignoring the color count (colors[0]) and the opacity(colors[1][-1])
palette = [colors[1][:-1] for colors in im.getcolors()]

# Add the background color (black) that'll replace the transparent background if present
if (0, 0, 0) not in palette:
    palette.append((0, 0, 0))

if len(palette) > 255:
    raise ValueError("Image has too many different colors, maximum allowed is 256")

h_sprite_size = 8
v_sprite_size = 8

h_image_size = im.size[0]
v_image_size = im.size[1]

if v_image_size % v_sprite_size or h_image_size % h_sprite_size:
    raise ValueError("Image size not multiples of sprite size")

# row number and sprite in row number
row = 0
sprite = 0

sprites = {}
for  i, px in enumerate(im.getdata()):
    sprite = (i % h_image_size) / h_sprite_size
    row = i / h_image_size / h_sprite_size

    if row not in sprites:
        sprites[row] = {}
    if sprite not in sprites[row]:
        sprites[row][sprite] = []

    if px[-1] == 0: px = (0, 0, 0, 255)
    sprites[row][sprite].append("0x%02X," % palette.index(px[:-1]))

# Flatten Sprite array
all_sprites = []
for row in sprites:
    for sprite in sprites[row]:
        all_sprites.append(sprites[row][sprite])
sprites = all_sprites

# pp.pprint(sprites)
print "const int total_number = %d;" % len(sprites)
print ""

print "const unsigned char palette[%d][3] = {" % len(palette)
for color in palette:
    print "\t{%d, %d, %d}," % color
print "};"
print ""

print "unsigned char sprites[%d][%d] PROGMEM = {" % (len(sprites), h_sprite_size * v_sprite_size)
for sprite_num, sprite in enumerate(sprites):
    colors = ""
    for indexed_color in sprite:
        colors += "%s " % indexed_color
    print "\t{%s}," % colors

print "};"
