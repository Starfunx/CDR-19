#ifndef PID_H
#define PID_H

#include <Arduino.h>

class PID
{
  public :
    // constructeur
    PID(float kp, float ki, float kd);
    // methodes
    float getnewCommand();

  private :
    float m_kp;
    float m_ki;
    float m_kd;

    float m_erreur_nm1;
};

#endif
