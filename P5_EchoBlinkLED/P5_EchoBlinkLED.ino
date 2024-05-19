int led = 13; //2, 3, 4, 5, .....13
int v;

void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  digitalWrite(led, HIGH);
  delay(1000);
  Serial.println("LED ENCENDIDO");
  digitalWrite(led, LOW);
  delay(1000);
  Serial.println("LED APAGADO");
  delay(1000);

}
