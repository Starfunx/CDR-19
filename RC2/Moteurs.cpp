#include "Moteur.h"

Moteur::Moteur(byte pin1, byte pin2, byte pin_vitesse ,float pwm_max, float speed_max, bool inverse_direction){
  m_pwm_max = pwm_max;
  m_speed_max = speed_max;
  m_pin_vitesse = pin_vitesse;
  if (inverse_direction){
    m_pin1 = pin2;
    m_pin2 = pin1;
  } else {
    m_pin1 = pin1;
    m_pin2 = pin2;
  }
  pinMode(m_pin1, OUTPUT);
  pinMode(m_pin2, OUTPUT);
  digitalWrite(m_pin1, LOW);
  digitalWrite(m_pin2, LOW);
  analogWrite(m_pin_vitesse,0);
}

Moteur::Moteur(byte pin1, byte pin2, byte pin_vitesse, float pwm_max, float speed_max){
  m_pwm_max = pwm_max;
  m_speed_max = speed_max;
  m_pin_vitesse = pin_vitesse;
  m_pin1 = pin2;
  m_pin2 = pin1;
  pinMode(m_pin1, OUTPUT);
  pinMode(m_pin2, OUTPUT);
  digitalWrite(m_pin1, LOW);
  digitalWrite(m_pin2, LOW);
  analogWrite(m_pin_vitesse,0);
}


void Moteur::setSpeed(byte vitesse){
  if (vitesse > 0){         // avancer
    digitalWrite(m_pin1, HIGH);
    digitalWrite(m_pin2, LOW);
  }
  else if (vitesse < 0) {   // reculer
    digitalWrite(m_pin1, LOW);
    digitalWrite(m_pin2, HIGH);
  }
  else {       // vitesse == 0 : arret
    digitalWrite(m_pin1, LOW);
    digitalWrite(m_pin2, LOW);
  }
  // conversion de vitesse en pwm et saturation
  vitesse = constrain(vitesse / m_speed_max * m_pwm_max, -m_pwm_max, m_pwm_max);
  analogWrite(m_pin_vitesse, vitesse);
}
