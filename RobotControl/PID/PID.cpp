#include "PID.h"


Pid::Pid(double kp, double ki, double kd){
  m_kp = kp;
  m_ki = ki;
  m_kd = kd;
  m_lastError = 0.0;
}

Pid::Pid(double kp, double ki, double kd, double Te){
  m_kp = kp;
  m_ki = ki;
  m_kd = kd;
  m_lastError = 0.0;
  m_Te = Te;
}


double Pid::getNewCommand(double error){
  double result = 0;
  result = m_kp * error;

  if (m_Te > 0 ){
      result = result + m_ki * (error + m_lastError)* m_Te
                      + m_kd * (error - m_lastError)/ m_Te;
  }
  else {
      result = result + m_ki * (error + m_lastError)
                      + m_kd * (error - m_lastError);
  }


  m_lastError = error;
  return result;
}
