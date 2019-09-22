#include "differentialDrive.h"

DifferentialDrive::DifferentialDrive(Motor *moteurGauche, Motor *moteurDroite, Pid *pidAngle, Pid *PidDistance){
  m_MoteurGauche  = moteurGauche;
  m_MoteurDroite  = moteurDroite;
  m_pidAngle  = pidAngle;
  m_pidFistance  = PidDistance;
}


void DifferentialDrive::newDiffCommands(double TargetDistance, double TargetAngle){

    if(abs(TargetAngle)< 0.02) TargetAngle = 0.0;
    // if(abs(TargetDistance)< 10) TargetDistance = 0.0;


    double commandeAngle, commandeDistance;
    commandeAngle = m_pidAngle->getNewCommand(TargetAngle);
    commandeDistance = m_pidFistance->getNewCommand(TargetDistance);

    double commandeGauche = commandeDistance + commandeAngle;
    double commandeDroite = commandeDistance - commandeAngle;

    int commandePWMGauche= map((long)commandeGauche, 1, 100, 68, 150);
    int commandePWMDroite= map((long)commandeDroite, 1, 100, 68, 150);

    if(commandeGauche == 0) commandePWMGauche = 0;
    if(commandeDroite == 0) commandePWMDroite = 0;

    if(commandeGauche<0)
      commandePWMGauche= -commandePWMGauche;

    if(commandeDroite<0)
      commandePWMDroite= -commandePWMDroite;

    if(abs(commandePWMGauche) <= 68)
      if(commandePWMGauche >0) commandePWMGauche = 68;
      else commandePWMGauche = -68;

      if(abs(commandePWMDroite) <= 68)
        if(commandePWMDroite >0) commandePWMDroite = 68;
        else commandePWMDroite = -68;

      // Serial.print(" commandeGauche : ");
      // Serial.print(commandeGauche);
      // Serial.print(" commandeDroite : ");
      // Serial.print(commandeDroite);

      Serial.print(" commandePWMGauche : ");
      Serial.print(commandePWMGauche);
      Serial.print(" commandePWMDroite : ");
      Serial.print(commandePWMDroite);
      Serial.print(" | ");


    m_MoteurGauche->setCommand(commandePWMGauche);
    m_MoteurDroite->setCommand(commandePWMDroite);
}
