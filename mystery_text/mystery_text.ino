// Robotics with the BOE Shield - ForwardLeftRightBackward
// Move forward, left, right, then backward for testing and tuning.

#include <Servo.h>                           // Include servo library

Servo servoLeft;                             // Declare left and right servos
Servo servoRight;
 
void setup()                                 // Built-in initialization block
{

  servoLeft.attach(13);                      // Attach left signal to pin 13
  servoRight.attach(12);                     // Attach right signal to pin 12

  // Full speed forward
  servoLeft.writeMicroseconds(1700);         // Left wheel counterclockwise
  servoRight.writeMicroseconds(1300);        // Right wheel clockwise
  delay(2000);                               // ...for 2 seconds

  // Turn left in place
  servoLeft.writeMicroseconds(1300);         // Left wheel clockwise
  servoRight.writeMicroseconds(1300);        // Right wheel clockwise
  delay(1000);                                // ...for 0.6 seconds

  // Turn right in place
  servoLeft.write(90);         // Left wheel counterclockwise
  servoRight.write(90);        // Right wheel counterclockwise
  delay(1000);                                // ...for 0.6 seconds

  //Turn right in place
  servoLeft.write(90);         // Left wheel counterclockwise
  servoRight.write(90);        // Right wheel counterclockwise
  delay(1000); 

  // Turn left in place
  servoLeft.writeMicroseconds(1300);         // Left wheel clockwise
  servoRight.writeMicroseconds(1300);        // Right wheel clockwise
  delay(1000); 

  
  // Full speed backward
  servoLeft.writeMicroseconds(1300);         // Left wheel clockwise
  servoRight.writeMicroseconds(1700);        // Right wheel counterclockwise
  delay(2000);                               // ...for 2 seconds

  servoLeft.detach();                        // Stop sending servo signals
  servoRight.detach();
}  

void loop()                                  // Main loop auto-repeats
{                                            // Empty, nothing needs repeating
}

