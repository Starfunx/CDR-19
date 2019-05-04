#include <Wire.h>
#define SLAVE_ADDRESS 0x04

#define MAX_CMD_SIZE 96
static uint8_t commandReceived[MAX_CMD_SIZE] = {0}; ///< Current received command.


void setup() {
  // Serial.begin(9600);
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  // Serial.println("Ready!");
}

void loop() {
  delay(100);
}



void receiveData(int byteCount) {
  // Serial.print("receiveData");
  commandReceived = {O};
  i=0;
  while(Wire.available())    // slave may send less than requested
  {
    char c = Wire.read();    // receive a byte as character
    // Serial.print(c);         // print the character
    commandReceived[i] = c;
    i++;
  }
  // serial.print(commandReceived)
  commandParse(commandReceived);
}


void sendData() {
  Wire.write(value);
}

void commandParse(char* command){



}
