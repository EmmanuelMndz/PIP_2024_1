double m, b, x, y;

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
  m = obtenerValor("Ingrese el valor de m...:");
  b = obtenerValor("Ingrese el valor de b...:");
  x = obtenerValor("Ingrese el valor de x...:");
  
  y = m * x + b;
  
  Serial.println("El resultado de Y = mx + b es: " + String(y));
}
