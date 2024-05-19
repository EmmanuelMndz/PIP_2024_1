double distancia, tiempo, velocidad;

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
  distancia = obtenerValor("Ingrese la distancia recorrida (en metros)...:");
  tiempo = obtenerValor("Ingrese el tiempo tomado (en segundos)...:");
  
  velocidad = distancia / tiempo;
  
  Serial.println("La velocidad es: " + String(velocidad) + " m/s");
}