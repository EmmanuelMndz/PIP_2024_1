char letra;
int ascii;

// Asignación de pines para los LEDs
const int ledPins[] = {2, 3, 4, 5, 6, 7, 8, 9};

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(10);

  // Configurar los pines de los LEDs como salidas
  for (int i = 0; i < 8; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
}

void loop() {
  if (Serial.available() > 0) {
    letra = Serial.read();
    if (letra != '\n') {
      ascii = (int)letra;
      Serial.print(letra);
      Serial.print(" == ");
      Serial.println(ascii);
      
      // Representar el valor ASCII en binario con LEDs
      for (int i = 0; i < 8; i++) {
        // Encender o apagar el LED correspondiente según el bit en la posición i
        digitalWrite(ledPins[i], (ascii >> i) & 1);
      }
      delay(1000); // Esperar un momento para visualizar los LEDs
    }
  }
}
