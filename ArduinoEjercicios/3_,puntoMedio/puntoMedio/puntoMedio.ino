
double MX, MY;
double x1,y1,x2,y2;

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
  Serial.println("Punto 1");
  x1 = obtenerValor("Ingresa el valor de x en el punto 1...:");
  y1 = obtenerValor("Ingresa el valor de y en el punto 1...:");
  Serial.println("Punto 1 (" + String(x1) + " , " + String(y1) + ")");
  Serial.println("Punto 2");
  x2 = obtenerValor("Ingresa el valor de x en el punto 2...:");
  y2 = obtenerValor("Ingresa el valor de y en el punto 2...:");
  Serial.println("Punto 2 (" + String(x2) + " , " + String(y2) + ")");
  MX = (x1+x2)/2;
  MY = (y1+y2)/2;
  Serial.println("Punto Medio: (" + String(MX) + " , " + String(MY) + ")");
  delay(2000);
}
