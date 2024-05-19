int LED[] = {2, 3, 4, 5, 6}; // Pines de los 5 LEDs
int numLeds;

void setup() {
  numLeds = sizeof(LED) / sizeof(int);
  for (int i = 0; i < numLeds; i++) {
    pinMode(LED[i], OUTPUT);
  }
  Serial.begin(9600);
  Serial.println("Seleccione un patrón:");
  Serial.println("1. Todos los LEDs encendidos y luego apagados");
  Serial.println("2. Parpadeo secuencial ascendente");
  Serial.println("3. Parpadeo secuencial descendente");
  Serial.println("4. Todos los LEDs encendidos y apagados alternativamente");
  Serial.println("5. Parpadeo rápido de todos los LEDs");
}

void loop() {
  if (Serial.available() > 0) {
    int patron = Serial.parseInt();

    switch (patron) {
      case 1:
        todosEncendidosYApagados();
        break;
      case 2:
        parpadeoAscendente();
        break;
      case 3:
        parpadeoDescendente();
        break;
      case 4:
        alternanciaEncendidoApagado();
        break;
      case 5:
        parpadeoRapido();
        break;
      default:
        Serial.println("Patrón inválido. Por favor, seleccione un patrón válido del 1 al 5.");
        break;
    }
  }
}
void todosEncendidosYApagados() {
  for (int i = 0; i < numLeds; i++) {
    digitalWrite(LED[i], HIGH);
  }
  delay(1000);
  for (int i = 0; i < numLeds; i++) {
    digitalWrite(LED[i], LOW);
  }
  delay(1000);
}

void parpadeoAscendente() {
  for (int i = 0; i < numLeds; i++) {
    digitalWrite(LED[i], HIGH);
    delay(200);
    digitalWrite(LED[i], LOW);
  }
}

void parpadeoDescendente() {
  for (int i = numLeds - 1; i >= 0; i--) {
    digitalWrite(LED[i], HIGH);
    delay(200);
    digitalWrite(LED[i], LOW);
  }
}

void alternanciaEncendidoApagado() {
  for (int i = 0; i < numLeds; i++) {
    digitalWrite(LED[i], HIGH);
    delay(200);
  }
  delay(1000);
  for (int i = 0; i < numLeds; i++) {
    digitalWrite(LED[i], LOW);
    delay(200);
  }
  delay(1000);
}

void parpadeoRapido() {
  for (int i = 0; i < 5; i++) {
    for (int j = 0; j < numLeds; j++) {
      digitalWrite(LED[j], HIGH);
    }
    delay(100);
    for (int j = 0; j < numLeds; j++) {
      digitalWrite(LED[j], LOW);
    }
    delay(100);
  }
}
