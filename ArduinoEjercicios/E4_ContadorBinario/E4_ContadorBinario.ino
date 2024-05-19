int led[] = {2, 3, 4, 5, 6, 7, 8, 9};
bool estado[] = {false, false, false, false, false, false, false, false};

void setup() {
  for(int i = 0; i < 8; i++) {
    pinMode(led[i], OUTPUT);
  }
}

void loop() {
  // Contador binario de 1 a 255
  for(int count = 1; count <= 255; count++) {
    // Convertir el contador a binario y actualizar el estado de los LED
    for(int i = 0; i < 8; i++) {
      estado[7 - i] = bitRead(count, i);
    }

    // Mostrar el estado actual de los LED
    for(int i = 0; i < 8; i++) {
      digitalWrite(led[i], estado[i]);
    }

    // Esperar 1 segundo
    delay(1000);
  }
}
