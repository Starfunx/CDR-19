#ifndef CONFIGURATION_H
#define CONFIGURATION_H

#include <Arduino.h>
#include "pin.h"


/*paramètres PID linéique */
float Kp_lin;
float Ki_lin;
float Kd_lin;

/*paramètres PID rotation */
float Kp_rot;
float Ki_rot;
float Kd_rot;


float resolution = 0.000109;  // en ticks/mm
float vitesse_max = 1;
float PWM_max = 255;

#endif
