#include "Odometrie.h"

Odometrie::Odometrie(
    Encoder* CodeurGauche, Encoder* CodeurDroite,
    double perimRoueG, double perimRoueD,
    double entreAxe, double resolutionCodeurs)
{
  m_CodeurG = CodeurGauche;
  m_CodeurD = CodeurDroite;

  m_perimRoueG = perimRoueG;
  m_perimRoueD = perimRoueD;
  m_entreAxe = entreAxe;
  m_resolutionCodeurs = resolutionCodeurs;

  m_x = 0;
  m_y = 0;
  m_th = 0;
}

void Odometrie::update(){

  double dGauche, dDroite;
  dGauche = (float)m_CodeurG->readAndReset() * m_perimRoueG / m_resolutionCodeurs;
  dDroite = (float)m_CodeurD->readAndReset() * m_perimRoueD / m_resolutionCodeurs;

  //Calcul de vitesse //w
  m_vG = dGauche / m_Te;//w
  m_vD = dDroite / m_Te;//w
  m_Vitesse = (m_vG + m_vD)/2;//w
  m_Omega = (m_vG - m_vD)/m_entreAxe;//w

  // Updating posiion
  //calcul de theta
  m_th = m_th + (dGauche - dDroite) / m_entreAxe;
  if ( m_th < -PI) m_th = m_th + 2*PI;
  if ( m_th >= PI) m_th = m_th - 2*PI;

  //calcul de xPos et yPos
  m_x = m_x + (dGauche + dDroite) / 2 * cos(m_th);
  m_y = m_y + (dGauche + dDroite) / 2 * sin(m_th);
}

void Odometrie::setXPosition(double x){
m_x = x;
}
void Odometrie::setYPosition(double y){
m_y = y;
}
void Odometrie::setThetaOrientation(double theta){
m_th = theta;
}


void Odometrie::GetPosition(double* x, double* y, double* theta){
  *x = m_x;
  *y = m_y;
  *theta = m_th;
}

void Odometrie::GetWheelsSpeeds(double* vitesseRoueGauche, double* vitesseRoueDroite){
  *vitesseRoueGauche = m_vG;
  *vitesseRoueDroite = m_vD;
}//w

void Odometrie::GetRobotSpeed(double* Vitesse, double* AngularSpeed){
  *Vitesse = m_Vitesse;
  *AngularSpeed = m_Omega;
}//w
