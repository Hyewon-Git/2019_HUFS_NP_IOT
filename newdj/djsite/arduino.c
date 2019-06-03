int motor_pin = 3;
int trig_pin = 8;
int echo_pin = 9;
int motor_speed = 255;
int motor_state = 1;

void setup() {
  Serial.begin(9600);
  pinMode(trig_pin, OUTPUT);
  pinMode(echo_pin, INPUT);
  pinMode(motor_pin, OUTPUT);
}

void loop() {
  digitalWrite(trig_pin, LOW);
  digitalWrite(echo_pin, LOW);
  delayMicroseconds(2);
  digitalWrite(trig_pin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig_pin, LOW);

  unsigned long duration = pulseIn(Echo, HIGH);

  float distance = duration / 29.0 / 2.0;

  if(distance < 10) {
   if (motor_state == 0){
      motor_state = 1;
      analogWrite(motor_pin, motor_speed);
      Serial.println(distance);
   }
  }
  else{
    if (motor_state == 1){
      motor_state = 0;
      analogWrite(motor_pin, LOW);
      Serial.println(distance);
   }
  }

  delay(500);

}