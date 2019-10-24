[![Project Status: Concept – Minimal or no implementation has been done yet, or the repository is only intended to be a limited example, demo, or proof-of-concept.](https://www.repostatus.org/badges/latest/concept.svg)](https://www.repostatus.org/#concept)

# Sprite Machine

This is a proof of concept to test displaying 8x8 RGB sprite animation on a
[ColorDuino](http://imall.iteadstudio.com/im120410004.html).

## Video

[Test video](http://www.youtube.com/watch?v=dKKWYTwNSV8)

## Project Description

As the Colorduino has a ATmega328P, with 32kB of flash and 2kB of RAM,
displaying sprite animations requires some tricks.

The spritesheet is first fed through a python script `spritesheet2h.py` that extracts the color
palette and then generates an Arduino source file with the indexed sprites data
stored in flash.

This gets compiled along with the rest of the code and when run, the indexed
color is read from flash for each pixel. It thus requires only a few bytes of memory
for any frames of the animation.

The generated data is available as an example in `src/spritesheet.h`.

## Requirements

[Python Imaging Library](http://www.pythonware.com/products/pil/)

## Current status

It's a proof of concept, it does nothing useful apart from displaying sprites.

## Credits

The included spritesheet is distributed with permission from Oryx at [Oryx
Design Lab](http://oryxdesignlab.com). You can find the complete sprite set
here: [LO-FI Horror sprite set](http://oryxdesignlab.com/sprites/arkham-shadows-sprite-set).
