#include <math.h>

double lado, n_lados, apotema, area;

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
  lado = obtenerValor("Ingrese la longitud de un lado del polígono...:");
  n_lados = obtenerValor("Ingrese el número de lados del polígono...:");
  apotema = obtenerValor("Ingrese la apotema del polígono...:");
  
  area = (n_lados * lado * apotema) / 2;
  
  Serial.println("El área del polígono regular es: " + String(area));
}
