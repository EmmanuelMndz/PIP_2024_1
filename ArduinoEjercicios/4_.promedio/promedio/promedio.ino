double promedio;
int n;

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
  n = obtenerValor("Ingrese el numero total de datos...:");
  for(int i = 0; i < n; i++){
    promedio += obtenerValor("Ingrese el valor # " + String(i+1) + "...:");
  }
  promedio = promedio / n;
  Serial.println("El promedio es : " + String(promedio));
}
