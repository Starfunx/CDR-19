#include "Motor.h"

Motor::Motor(byte pin1, byte pin2, byte pin_pwm, float pwm_min, float pwm_max, bool inverse_direction){
  m_min_pwm = pwm_min;
  m_max_pwm = pwm_max;

  m_pin_pwm = pin_pwm;
  if (inverse_direction){
    m_pin1 = pin2;
    m_pin2 = pin1;
  } else {
    m_pin1 = pin1;
    m_pin2 = pin2;
  }
  pinMode(m_pin1, OUTPUT);
  pinMode(m_pin2, OUTPUT);
  digitalWrite(m_pin1, LOW);
  digitalWrite(m_pin2, LOW);
  analogWrite(m_pin_pwm, 0);
}

Motor::Motor(byte pin1, byte pin2, byte pin_pwm,float pwm_min, float pwm_max){
  m_min_pwm = pwm_min;
  m_max_pwm= pwm_max;

  m_pin_pwm = pin_pwm;
  m_pin1 = pin2;
  m_pin2 = pin1;
  pinMode(m_pin1, OUTPUT);
  pinMode(m_pin2, OUTPUT);
  digitalWrite(m_pin1, LOW);
  digitalWrite(m_pin2, LOW);
  analogWrite(m_pin_pwm,0);
}

// sets the motor's direction to forward
void Motor::setFwd()
{
  digitalWrite(m_pin1, HIGH);
  digitalWrite(m_pin2, LOW);
}

// sets the motor's direction to backward
void Motor::setBack()
{
  digitalWrite(m_pin1, LOW);
  digitalWrite(m_pin2, HIGH);
}

// sets the motor to freewheel
void Motor::setFree()
{
  digitalWrite(m_pin1, LOW);
  digitalWrite(m_pin2, LOW);
}

// sets the motor to brake
void Motor::setStop()
{
  digitalWrite(m_pin1, HIGH);
  digitalWrite(m_pin2, HIGH);
}

// accepts an int, the PWM level, as a parameter
// sets the PWM output to the motor to the given int
// level must be between 0 and 255 inclusive
// behavior is undefined if level is outside this range
void Motor::setPWM(int level)
{
	analogWrite(m_pin_pwm, level);
}


void Motor::setCommand(int signedPwm){
  if (signedPwm > 0){
    setFwd();
  }
  else if (signedPwm < 0){
    setBack();
  }
  else {
    setFree();
  }

  setPWM(abs(signedPwm));

}
