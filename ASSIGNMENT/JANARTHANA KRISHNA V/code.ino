// C++ code
//
int sensorValue = 0;

void setup()
{
  pinMode(A0, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop()
{
  // read the value from the sensor
  sensorValue = analogRead(A0);
  // turn the LED on
  digitalWrite(LED_BUILTIN, HIGH);
  // pause the program for <sensorValue> millseconds
  delay(sensorValue); // Wait for sensorValue millisecond(s)
  // turn the LED off
  digitalWrite(LED_BUILTIN, LOW);
  // pause the program for <sensorValue> millseconds
  delay(sensorValue); // Wait for sensorValue millisecond(s)
}