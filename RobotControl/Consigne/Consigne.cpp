#include "Consigne.h"


/* constructeur: x y et theta correspondant à la position du robot par defaut
                 cela pour ne pas déplacer le robot initialement
*/
Consigne::Consigne(double x, double y, double theta)
{
  m_x_c  = x;
  m_y_c  = y;
  m_theta_c  = theta;
}


void Consigne::setConsigne(double x_c, double y_c, double theta_c){
  m_x_c  = x_c;
  m_y_c  = y_c;
  m_theta_c  = theta_c;
}


void Consigne::getConsigne(double* x_c, double* y_c, double* theta_c){
  *x_c  = m_x_c;
  *y_c  = m_y_c;
  *theta_c  = m_theta_c;
}

void Consigne::getsNewError(double* distance, double* cap, double x, double y, double theta){

    processNewError(x, y, theta);
    *distance = m_dist;
    *cap = m_cap;

}



void Consigne::getsNewError(double* distance, double* cap, double x, double y, double theta,
                  double* erreurX, double* erreurY, double* erreurCap ){
    processNewError(x, y, theta);
    *distance = m_dist;
    *cap = m_cap;
    *erreurX = m_erreurX;
    *erreurY = m_erreurY;
    *erreurCap = m_erreurCap;
}


void Consigne::processNewError(double x, double y, double theta){

  m_erreurX = m_x_c - x;
  m_erreurY = m_y_c - y;
  m_erreurCap =  m_theta_c - theta;

  m_dist = sqrt( pow(m_x_c-x,2) + pow(m_y_c-y,2));
  m_cap = atan2( m_y_c-y, m_x_c-x) - theta;

  if ( m_cap < -PI) m_cap = m_cap + 2*PI;
  if ( m_cap >= PI) m_cap = m_cap - 2*PI;

  if (m_cap < -PI/2) {
    m_cap = m_cap + PI;
    if ( m_cap < -PI) m_cap = m_cap + 2*PI;
    if ( m_cap >= PI) m_cap = m_cap - 2*PI;

    m_dist = -m_dist;
  }

}
