#ifndef MOTOR_H
#define MOTOR_H

#include <Arduino.h>

class Motor
{
  public :
    // constructeur
    Motor(byte pin1, byte pin2, byte pin_pwm, float m_pwm_min, float pwm_max, bool inverse_direction);
    Motor(byte pin1, byte pin2, byte pin_pwm, float m_pwm_min, float pwm_max);
    // methodes
    void setFwd();
    void setBack();
    void setFree();
    void setStop();
    void setPWM(int level);

    void setCommand(int signedPwm);

  private :
    byte m_pin1;
    byte m_pin2;
    byte m_pin_pwm;

    int m_min_pwm;
    int m_max_pwm;
};

#endif
