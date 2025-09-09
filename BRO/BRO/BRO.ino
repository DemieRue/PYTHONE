const int analogInPin1 = A0;  
const int analogInPin2 = A1;  
int sensorValue[2];        
float voltageValue[2];       
unsigned long lastTime = 0 , sampleTime = 200; 

void setup() {
  
  Serial.begin(9600);
}

void loop() {
  if(millis()-lastTime>sampleTime){
  lastTime = millis();
  
  sensorValue[0] = analogRead(analogInPin1);
  sensorValue[1] = analogRead(analogInPin2);
  
  voltageValue[0] = scaling(sensorValue[0], 0, 1023, 0, 5);
  voltageValue[1] = scaling(sensorValue[1], 0, 1023, 0, 5);
  
  Serial.println(voltageValue[0]); 
  Serial.println(voltageValue[1]);  
  Serial.println(random(-50,50));  
  Serial.println(random(0,100));   
  }
}

float scaling(float x, float in_min, float in_max, float out_min, float out_max) 
{
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}
