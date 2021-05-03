/*   
HC05 - Bluetooth AT-Command mode  
modified on 10 Feb 2019 
by Saeed Hosseini 
https://electropeak.com/learn/ 
*/ 
/*
 * When paired, two fast blinks followed by about 1sec gap seems to indicate 'working'
 */



 /*
  * 
  * To be paired with c:\Alan\Arduino\PC_Comms_20210429T2019
  * BT is HC05
  * BT Pin 2   5V
  * BT Pin 3 GND
  * BT Pin 4 BLUE Arduino Pin 2
  * BT Pin 5 Orange to splitter
  * 
  * Check out page 97 of BOE for Arduino.pdg
  */
#include <SoftwareSerial.h> 
#include <Servo.h> // Include servo library

Servo servoRight; // Declare right servo
Servo servoLeft; // Declare left servo

SoftwareSerial MyBlue(2, 3); // RX | TX 
int flag = 0; 
int LED = 8; 
int speed_left = 1500;
int speed_right = 1500;
void setup() 
{
  servoLeft.attach(10); // Attach left signal to pin 10
  servoRight.attach(11); // Attach right signal to pin 11
  Serial.begin(9600); 
 MyBlue.begin(9600); 
// the setup function runs once when you press reset or power the board
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.println("Ready to connect\nDefualt password is 1234 or 000"); 
} 
void loop() 
{ 

  
 if (MyBlue.available()) 
   flag = MyBlue.read(); 
   //flag = Serial.read();
 //Serial.println(flag);

 if (flag == 75)  //;t
 {
    speed_left -= 10;
    speed_right -=10;
 }
 else if (flag == 77) //rt
 {
    speed_left += 10;
    speed_right +=10;
 }  
 else if (flag == 80) //dn
 {
    speed_left -= 10;
    speed_right +=10;
 }  
  else if (flag == 72) // up
 {
    speed_left += 10;
    speed_right -=10;
 }  
  else if (flag == 32)
 {
    speed_left = 1460;
    speed_right = 1480;
 }  
if (flag > 0)
{
  
      Serial.println(flag);
      flag = 0;
      Serial.println("Speed_right = ");
      Serial.println(speed_right);
      Serial.println("Speed_left= ");
      Serial.println(speed_left);

}
    servoRight.writeMicroseconds(speed_right);
    servoLeft.writeMicroseconds(speed_left); 
 
      
// if (flag == 49) 
// { 
//   digitalWrite(LED_BUILTIN, HIGH); 
//   Serial.println("LED On"); 
// } 
// else if (flag == 48) 
// { 
//   digitalWrite(LED_BUILTIN, LOW); 
//   Serial.println("LED Off"); 
// } 
}
