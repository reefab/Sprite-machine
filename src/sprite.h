#include <Colorduino.h>
#include <avr/pgmspace.h>
#include "spritesheet.h"

void display_sprite(int i) {
  unsigned char x,y, pixel, color;

  pixel = 0;
  for(y = 0; y < ColorduinoScreenHeight; y++) {
    for(x = 0; x < ColorduinoScreenWidth; x++) {
        color = pgm_read_byte(&(sprites[i][pixel])); // get pixel indexed color from flash
        Colorduino.SetPixel(x, y, palette[color][0], palette[color][1], palette[color][2]);
        pixel++;
      }
  }
  Colorduino.FlipPage(); // swap screen buffers to show it
}

void sprite_anim() {
  int i;
  for (i =0; i < total_number;i++) {
      display_sprite(i);
      delay(200);
  }
}
