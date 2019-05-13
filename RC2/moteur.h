#ifndef MOTOR_H
#define MOTOR_H

#include <Arduino.h>

class Moteur
{
  public :
    // constructeur
    Moteur(byte pin1, byte pin2, byte pin_vitesse, float m_pwm_min, float pwm_max, float speed_max, bool inverse_direction);
    Moteur(byte pin1, byte pin2, byte pin_vitesse, float m_pwm_min, float pwm_max, float speed_max);
    // methodes
    void setSpeed(byte vitesse);

  private :
    byte m_pin1;
    byte m_pin2;
    byte m_pin_vitesse;

    float m_speed_max;
    float m_pwm_max;
};

#endif
