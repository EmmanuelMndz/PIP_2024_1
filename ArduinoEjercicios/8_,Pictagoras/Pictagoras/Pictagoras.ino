#include <math.h>

double cateto1, cateto2, hipotenusa;

double obtenerValor(String msg){
  Serial.print(msg);
  while(Serial.available() == 0){}
  double valor = Serial.readString().toDouble();
  Serial.println(" " + String(valor));
  return valor;
}

void setup() {
  Serial.begin(9600);
}

void loop() {
  cateto1 = obtenerValor("Ingrese la longitud del primer cateto...:");
  cateto2 = obtenerValor("Ingrese la longitud del segundo cateto...:");
  
  hipotenusa = sqrt(pow(cateto1, 2) + pow(cateto2, 2));
  
  Serial.println("La longitud de la hipotenusa es: " + String(hipotenusa));
}
