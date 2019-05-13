#include "PID.h"

PID::PID(float kp, float ki, float kd){
    m_kp = kp;
    m_ki = ki;
    m_kd = kd;
}

float PID::getnewCommand(float error){
    result =  kp*(error)
            + ki*(error + m_error_nm1)
            + kd*(error - m_error_nm1);
    m_erreur_nm1 = error; // reindexation
    return result;
}
