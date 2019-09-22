#ifndef DIFFDRIVE_H
#define DIFFDRIVE_H

#include <Arduino.h>
#include <Motor.h>
#include "PID.h"
// #include "configuration.h"

class DifferentialDrive
{
  public :
    // constructeur
    DifferentialDrive(Motor *moteurGauche, Motor *moteurDroite, Pid *pidAngle, Pid *PidDistance);

    void newDiffCommands(double TargetDistance, double TargetAngle);

  private :
  Motor *m_MoteurGauche, *m_MoteurDroite;
  Pid *m_pidAngle, *m_pidFistance;

};

#endif
