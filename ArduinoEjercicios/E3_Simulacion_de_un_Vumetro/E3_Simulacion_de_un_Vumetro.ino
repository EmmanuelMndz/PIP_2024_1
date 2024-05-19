int ledPins[] = {2, 3, 4, 5, 6};
int valor;

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 5; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
}

void loop() {
  valor = analogRead(A0);
  Serial.println("Valor del vumetro: " + String(valor));
  
  for (int i = 0; i < 5; i++) {
    if (valor > (i * 205)) {
      digitalWrite(ledPins[i], HIGH);
    } else {
      digitalWrite(ledPins[i], LOW);
    }
  }

  // Esperar 1 segundo
  delay(1000);
}
