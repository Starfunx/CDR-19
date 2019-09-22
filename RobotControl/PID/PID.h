#ifndef PID_H
#define PID_H

#include <Arduino.h>

class Pid
{
  public :
    // constructeur
    Pid(double kp, double ki, double kd);
    Pid(double kp, double ki, double kd, double Te);

    double getNewCommand(double error);

  private :
  double m_kp, m_ki, m_kd;
  double m_lastError;

  double m_Te = -1;
};

#endif
