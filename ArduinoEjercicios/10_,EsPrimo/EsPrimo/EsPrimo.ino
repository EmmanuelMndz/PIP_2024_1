bool esPrimo(int numero) {
  if (numero <= 1) {
    return false;
  }
  for (int i = 2; i <= sqrt(numero); i++) {
    if (numero % i == 0) {
      return false;
    }
  }
  return true;
}

void setup() {
  Serial.begin(9600);
}

void loop() {
  int num;
  Serial.print("Ingrese un número...: ");
  while(Serial.available() == 0){}
  num = Serial.readString().toInt();
  Serial.println(String(num));
  
  if (esPrimo(num)) {
    Serial.println("El número es primo.");
  } else {
    Serial.println("El número no es primo.");
  }
}
