double peso, altura, imc;

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
  Serial.println("Por favor, introduzca su peso (en kg) y su altura (en metros):");
  
  peso = obtenerValor("Ingrese su peso (kg): ");
  altura = obtenerValor("Ingrese su altura (m): ");
  
  imc = peso / (altura * altura);
  
  Serial.print("Su Índice de Masa Corporal (IMC) es: ");
  Serial.println(imc);
}

