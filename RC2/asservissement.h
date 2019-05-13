#include <Arduino.h>
#include "codeurs.h"
#include "moteur.h"
#include "PID.h"

Moteur MG(PIN_MoteurGauche_1, PIN_MoteurGauche_2, PIN_PWMMoteurGauche, PWM_min, PWM_max, vitesse_max);
Moteur MD(PIN_MoteurDroit_1,  PIN_MoteurDroit_2, PIN_PWMMoteurDroit, PWM_min, PWM_max, vitesse_max);

PID pidDistance(Kp_lin, Ki_lin, Kd_lin);
PID pidOrientation(Kp_rot, Ki_rot, Kd_rot);

/*
convertit les ticks en mm
*/
float tick_to_meter(int nb_tops){
  return (float)nb_tops * resolution;
}

void asser(float consigne_distance, float consigne_orientation){

  float position_G;
  float position_D;
  float erreur_distance;
  float erreur_orientation;
  float commande_mot_D;
  float commande_mot_G;

  erreur_position_G = consigne_distance -  tick_to_meter(CompteurGauche);
  erreur_position_D = consigne_orientation - tick_to_meter(CompteurDroit);

  erreur_distance    =   (erreur_position_G + erreur_position_D)/2;
  erreur_orientation =   (erreur_position_G - erreur_position_D);

  commande_G = pidDistance.getnewCommand(erreur_distance)
                - pidOrientation.getnewCommand(erreur_orientation);

  commande_D = pidDistance.getnewCommand(erreur_distance)
                + pidOrientation.getnewCommand(erreur_orientation);

  MG.setSpeed(commande_G);
  MD.setSpeed(commande_D);
}
