#ifndef CONFIGURATION_H
#define CONFIGURATION_H

#include <Arduino.h>
#include "pins.h"

#ifndef PI
#define PI 3.14//15926535897932384626433832795
#endif
// paramètres codeurs
double coder_resolution =2400/2*PI ;  // en tick par rad

// paramètres geometriques des roues odometriques
float CoeffCorrecteurWheel = 1;
float leftCoderWheelPerimeter = 377; // mm
float rightCoderWheelPerimeter = CoeffCorrecteurWheel * leftCoderWheelPerimeter; // mm
float entreAxeRoueCodeuses = 123; // mm



// paramètres controle diferentiel
float kp_angle = 30 , ki_angle = 0.0, kd_angle = 600;
float kp_dist = 0.02, ki_dist = 0.0, kd_dist = 0.0;

// paramètres moteurs
int pwm_min = 0;
int pwm_max = 150;

int seuil = 800;
double resSharp = 4.8828;

//Conditions initiales
// position de départ
double x0 = 0;
double y0 = 0;
double theta0 = 0;
#endif
