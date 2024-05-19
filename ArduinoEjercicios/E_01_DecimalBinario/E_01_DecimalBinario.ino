int led[] = {2, 3, 4, 5, 6, 7, 8, 9};
bool estado[] = {false, false, false, false, false, false, false, false};
int aux = 0;
int temp;

void setup() {
  // put your setup code here, to run once:
  for(int i = 0; i < 8; i++){
    pinMode(led[i], OUTPUT);
  }
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0){
    temp = Serial.readString().toInt();
    while(temp > 0){
      estado[7 - aux] = (temp % 2 == 1) ?true :false;
      temp = (int)temp / 2;
      aux++;
    }

    for(int i = 0; i < 8; i++){
      digitalWrite(led[i], estado[i]);
      estado[i] = false;
    }
    aux = 0;
  }
}