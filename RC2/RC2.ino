
#include <Arduino.h>

#include "configuration.h"
#include "asservissement.h"
#include "lib/TimerThree-master/TimerThree.h"

void setup()
{
  Serial.begin(9600);

  // definition codeurs
  attachInterrupt(digitalPinToInterrupt(PIN_CodeurDroit_A), InterruptionCodeurDroit_A, CHANGE);
  attachInterrupt(digitalPinToInterrupt(PIN_CodeurDroit_B), InterruptionCodeurDroit_B, CHANGE);
  attachInterrupt(digitalPinToInterrupt(PIN_CodeurGauche_A), InterruptionCodeurGauche_A, CHANGE);
  attachInterrupt(digitalPinToInterrupt(PIN_CodeurGauche_B), InterruptionCodeurGauche_B, CHANGE);

  Timer3.initialize(50000); // délai
  Timer3.attachInterrupt(scenario()); // ajouter une fonction de call back
}

void loop()
{

}


void scenario(){

}

void recalage(){
  
}
