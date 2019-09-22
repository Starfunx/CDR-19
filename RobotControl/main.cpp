#include <Arduino.h>
#include <Encoder.h>

#include "configuration.h"
#include <Odometrie.h>
#include <Consigne.h>
#include <PID.H>
#include <Motor.h>
#include <DifferentialDrive.h>
#include <sharp.h>

Encoder EncodeurGauche(PIN_CodeurGauche_A, PIN_CodeurGauche_B);
Encoder EncodeurDroite(PIN_CodeurDroit_A, PIN_CodeurDroit_B);

Odometrie Odometre(&EncodeurGauche, &EncodeurDroite,
    leftCoderWheelPerimeter, rightCoderWheelPerimeter,
    entreAxeRoueCodeuses, coder_resolution);

Consigne consigne( x0, y0, theta0);

Motor MoteurGauche(PIN_MoteurGauche_1, PIN_MoteurGauche_2, PIN_PWMMoteurGauche, pwm_min, pwm_max);
Motor MoteurDroite(PIN_MoteurDroit_1, PIN_MoteurDroit_2, PIN_PWMMoteurDroit, pwm_min, pwm_max);

Pid pidAngle(kp_angle, ki_angle, kd_angle);
Pid pidRotation(kp_dist, ki_dist, kd_dist);

DifferentialDrive differentiel(&MoteurGauche, &MoteurDroite, &pidAngle, &pidRotation);


int Te = 5; // periode d'échantillonage en millisecondes
unsigned long t0,t; // time at the t instant

double x, y, theta;// position du robot
double x_c, y_c, theta_c;

double distance, cap;
double distanceParcourue = 0.0;

double tfin = 50; // 50 secondes avant arrêt total.


void fin(){
  MoteurGauche.setFree();
  MoteurDroite.setFree();
  while (true) {
    Serial.print("salut je m'en bat les couilles \n");
  }
}

void setup() {

  while(digitalRead(PIN_tirette) == true){
    Serial.print("en attente que tu me tires (les couilles, toujours)  \n");
  }

  t0 = millis();

  // put your setup code here, to run once:
  Serial.begin(921600);
  Odometre.setXPosition(x0);
  Odometre.setYPosition(y0);
  Odometre.setThetaOrientation(theta0);

}


void loop() {

  if ( (double)t/1000 >= tfin) fin(); // condition d'arret definitif robot.

  Detection_obstacle_AR();
  while (detection_AR){ // arret temporaire pour cause d'obstacle.
    MoteurGauche.setFree();
    MoteurDroite.setFree();
    Detection_obstacle_AR();
    Serial.print("Degage, tu me casses les couilles!! \n");
  }

  // put your main code here, to run repeatedly:
  t = millis() - t0;
  if (t/Te > 1 ){
    Odometre.update();
    Odometre.GetPosition(&x, &y, &theta);
    double robotSpeed, omegaSpeed;
    Odometre.GetRobotSpeed(&robotSpeed, &omegaSpeed);
     // recupere l'erreur de cap et de distance
    // consigne.getsNewError(&distance, &cap, x, y, theta);
    // consigne.setConsigne(0, 0, PI/2);
    // consigne.setConsigne(200, 200, 0);

    distanceParcourue += abs(robotSpeed * Te);

    consigne.setConsigne( 3000, y, 0);
    consigne.getsNewError(&distance, &cap, x, y, theta);

    differentiel.newDiffCommands(distance, cap);



    // affichages

    // Serial.print("t(s): ");
    // Serial.print((float)t/1000, 3);
    // Serial.print(" | ");

    consigne.getConsigne(&x_c, &y_c, &theta_c);
    // MoteurGauche.setCommand(150);
    // delay(5000);
    // MoteurGauche.setCommand(-150);
    // delay(5000);

    // Serial.print(" distance: ");
    // Serial.print(distance);
    // Serial.print(" cap: ");
    // Serial.print(cap);

    Serial.print(" | ");

    Serial.print(" x_c: ");
    Serial.print(x_c);
    // Serial.print(" y_c: ");
    // Serial.print(y_c);

    // Serial.print(" theta_c: ");
    // Serial.print(theta_c);

    Serial.print(" x: ");
    Serial.print(x);
    Serial.print(" y: ");
    Serial.print(y);

    // Serial.print(" theta: ");
    // Serial.print(theta);


    Serial.print(" | ");

    Serial.print(" distance: ");
    Serial.print(distance);
    Serial.print(" cap: ");
    Serial.print(cap);
    // Serial.print(" cap+PI: ");
    // Serial.print(cap + PI);

    Serial.print("\n");

  }

}
