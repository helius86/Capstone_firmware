int P_SWITCH = 4; // digital pin
float grams_force;

#include "HX711.h"

double calibration_factor = 3150; // 45.93 grams for golf ball
double current_time;
double prev_time;
double rate;
double creep;

//double count;
//long randNumber; //used for testing

#define DOUT  25
#define CLK  26
#define FS 500
//#define zero -57598
// creep 0.000036 g / ms
HX711 scale;

void setup() {
  // put your setup code here, to run once:
  pinMode(P_SWITCH, INPUT);
  //Serial.begin(9600);
  Serial.begin(115200);


//comment if no electronics

  scale.begin(DOUT, CLK);
  
  scale.set_scale(calibration_factor); //This value is obtained by using the SparkFun_HX711_Calibration sketch
  scale.tare(); //Assuming there is no weight on the scale at start up, reset the scale to 0


  current_time = 0;
  prev_time = 0;
  creep = 0.05*500.0 *(1/3.0)*(1/60.0)*(1/1000.0)*10.0; // %FS / 3min * 1min/60s = creep in g /10ms

  //count = 0; //only used as dummy data


}

void loop() {
  // put your main code here, to run repeatedly:

  //randNumber = random(0,100);
  //grams_force = 2; //randNumber; //use if no electronics
  grams_force = scale.get_units(); //comment out if no electronics
  current_time = millis();
  if (current_time - prev_time >= 10) {
    prev_time = millis();
    grams_force -= creep;
  }
  
  
/* FORMAT of data sent to GUI
* Button's activation status: "0" OR "1"
* semicolon: ";"
* measured force: [float]
* semicolon: ";"
* measured distance: (float)
* semiconlon: ";"
* position: (char)
*/

  
  //Serial.print("Button: ");
  //randNumber = random(0,2);
  
  //Serial.print(1);//randNumber); //use in place of digitalRead(P_SWITCH) if no electronics
  Serial.print(digitalRead(P_SWITCH)); //comment out if there's not electronics connected

  Serial.print(";");
  
  //Serial.print(" Grams-Force: ");
  Serial.print(grams_force, 4);

/*
  Serial.print(";");

  //Serial.print(" Distance: ");
  randNumber = random(1,11);
  randNumber *= 0.12
  Serial.print(randNumber, 4);

  */
    
 // Serial.print(" gf   Creep: ");
 // Serial.print(creep, 20);
 

  //if (current_time >= 180000) {
    //  rate = (grams_force - 45.93)/current_time;
  //}
  //Serial.print(" Actual Creep: ");
  //Serial.print(rate, 20);
  Serial.println();

//  count += 0.1;

//  delay(1000);
  
}
