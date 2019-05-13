#include <Arduino.h>
#include "configuration.h"

float CompteurGauche;
float CompteurDroit;

void InterruptionCodeurDroit_A(){
  if (digitalRead(CodeurGauche_B) == digitalRead(CodeurGauche_A))
      CompteurGauche--;
    else
      CompteurGauche++;
}

void InterruptionCodeurDroit_B() {
  if (digitalRead(CodeurDroit_A) == digitalRead(CodeurDroit_B))
      CompteurDroit++;
  else
      CompteurDroit--;
}

void InterruptionCodeurGauche_A(){
  if (digitalRead(CodeurGauche_B) == digitalRead(CodeurGauche_A))
      CompteurGauche--;
  else
      CompteurGauche++;
}

void InterruptionCodeurGauche_B() {
  if (digitalRead(PIN_CodeurGauche_A) == digitalRead(CodeurGauche_B))
      CompteurDroit++;
  else
      CompteurDroit--;
}
