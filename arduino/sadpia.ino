int sensor_temperatura = A0;
int led_frio = 12;
int led_calor = 8;

void setup() {
  Serial.begin(9600);
  pinMode(led_frio, OUTPUT);
  pinMode(led_calor, OUTPUT);
  pinMode(sensor_temperatura, INPUT);
}

void loop() {
  int lectura = analogRead(sensor_temperatura);
  
  float voltaje = lectura * 5.0 / 1023.0;
  float temperatura = (voltaje - 0.5) * 100.0;
  
  Serial.print("Temperatura °C: ");
  Serial.println(temperatura);

  if(temperatura > 26.0) {
    digitalWrite(led_calor, HIGH);
    digitalWrite(led_frio, LOW);
  } else if(temperatura < 24.0) {
    digitalWrite(led_frio, HIGH);
    digitalWrite(led_calor, LOW);
  }

  delay(200);
}
