#ifndef ODOMETRIE_H
#define ODOMETRIE_H

#include <Encoder.h>

#ifndef PI
#define PI 3.1415926535897932384626433832795
#endif

class Odometrie{

public:
  // constructeur
  Odometrie(
      Encoder* CodeurGauche, Encoder* CodeurDroite,
      double perimRoueG, double perimRoueD,
      double entreAxe, double resolutionCodeurs);

  void update();

  // setters
  void setXPosition(double x);
  void setYPosition(double y);
  void setThetaOrientation(double theta);

  //assenceurs
  void GetPosition(double* x, double* y, double* theta);

  void GetWheelsSpeeds(double* vitesseRoueGauche, double* vitesseRoueDroite);//w
  void GetRobotSpeed(double* Vitesse, double* AngularSpeed);//w

private:
  double m_perimRoueG, m_perimRoueD, m_entreAxe;
  double m_resolutionCodeurs;

  double m_x, m_y, m_th;
  double m_vG, m_vD;
  double m_Vitesse, m_Omega;

  Encoder *m_CodeurG, *m_CodeurD;

  double m_Te = 5e-3;//Te en seconde //w
};


#endif
