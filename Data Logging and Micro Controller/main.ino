#include <SparkFun_Bio_Sensor_Hub_Library.h>
#include <Wire.h>

int samples = 400; //max number of samples/sec that covers maximum pulse width
int pulsewidth = 411 //largest pulse width
int sampleVal;
int pulsewidthVal;
int resPin = 4;
int mfioPin = 5;
int sensorVals[] = {0,0,0}; //to send data: BPM, O2, Confidence

SparkFun_Bio_Sensor_Hub bioHub(resPin, mfioPin); 
bioData body;  

void setup(){

  Serial.begin(115200);

  Wire.begin();
  int result = bioHub.begin();
  if (result == 0) {// Zero errors!
    Serial.println("Sensor started!");
  }
  else
  {
	  Serial.println("Could not communicate with the sensor!!!");
  }
 
//configure sensor to mode 1
  Serial.println("Configuring Sensor...."); 
  int error = bioHub.configBpm(MODE_ONE); // Configuring just the BPM settings. 
  if(error == 0){ // Zero errors!
    Serial.println("Sensor configured.");
  }
  else {
    Serial.println("Error configuring sensor.");
    Serial.print("Error: "); 
    Serial.println(error); 
  }
  
  //Check pulse width
  error = bioHub.setPulseWidth(width);
  if (error == 0){// Zero errors.
    Serial.println("Pulse Width Set.");
  }
  else {
    Serial.println("Could not set Pulse Width.");
    Serial.print("Error: "); 
    Serial.println(error); 
  }
  
    // Data lags a bit behind the sensor, if you're finger is on the sensor when
  // it's being configured this delay will give some time for the data to catch
  // up. 
  Serial.println("Loading up the buffer with data....");
  delay(4000); 
  
}

void loop(){

    // Information from the readSensor function will be saved to our "body"
    // variable.  
    body = bioHub.readSensorBpm();
    Serial.print("Infrared LED counts: ");
    Serial.println(body.irLed); 
    Serial.print("Red LED counts: ");
    Serial.println(body.redLed); 
    Serial.print("Heartrate: ");
    Serial.println(body.heartRate); 
    Serial.print("Confidence: ");
    Serial.println(body.confidence); 
    Serial.print("Blood Oxygen: ");
    Serial.println(body.oxygen); 
    Serial.print("Status: ");
    Serial.println(body.status); 
    // Slow it down or your heart rate will go up trying to keep up
    // with the flow of numbers
    delay(250); 
}

void main (){
	
	
	sensorVal[0] = body.heartRate;
	sensorVal[1] = body.oxygen;
	sensorVal[2] = body.confidence;
	delay(100)
}
	

