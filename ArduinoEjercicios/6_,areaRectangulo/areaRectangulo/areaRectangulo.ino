double base, altura, area;

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
  base = obtenerValor("Ingrese la base del rectángulo...:");
  altura = obtenerValor("Ingrese la altura del rectángulo...:");
  
  area = base * altura;
  
  Serial.println("El área del rectángulo es: " + String(area));
}
