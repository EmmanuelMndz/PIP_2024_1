#include <math.h>

double x1, y1, x2, y2, distancia;

double obtenerValor(String msg){
  Serial.print(msg);
  while(!Serial.available()){}
  double valor = Serial.readString().toDouble();
  Serial.println(valor);
  return valor;
}

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println("Por favor, introduzca las coordenadas de los puntos:");
  
  x1 = obtenerValor("Ingrese la coordenada x del primer punto: ");
  y1 = obtenerValor("Ingrese la coordenada y del primer punto: ");
  x2 = obtenerValor("Ingrese la coordenada x del segundo punto: ");
  y2 = obtenerValor("Ingrese la coordenada y del segundo punto: ");
  
  distancia = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
  
  Serial.print("La distancia entre los dos puntos es: ");
  Serial.println(distancia);
}
