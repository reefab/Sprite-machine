#include <Colorduino.h>
#include "sprite.h"

void setup() {
    Serial.begin(9600);
    while (!Serial) {;}
    Serial.println("console started");

    Colorduino.Init(); // initialize the board

    // compensate for relative intensity differences in R/G/B brightness
    // array of 6-bit base values for RGB (0~63)
    // whiteBalVal[0]=red
    // whiteBalVal[1]=green
    // whiteBalVal[2]=blue
    unsigned char whiteBalVal[3] = {15,63,50}; // for LEDSEE 6x6cm round matrix
    Colorduino.SetWhiteBal(whiteBalVal);
}

void loop() {
    sprite_anim();
}
