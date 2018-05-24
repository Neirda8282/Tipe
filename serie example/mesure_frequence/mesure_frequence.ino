long t1 = 0; // premier seuil
long t2 = 0; // deuxime seuil
float deltat;
float f;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(22,INPUT);
  attachInterrupt(22,freq,CHANGE);
  // temps = millis();  //recupere le temps depuis le chronometre de l'arduino
}

void loop() {
  // put your main code here, to run repeatedly:
  deltat=deltat*(10^6)/6;
  Serial.println(deltat);
  f = (1/deltat);
  //delay(500);
}
void freq() {
  t1 = t2;
  t2 = micros();
  deltat = (t2-t1);

  //Serial.println(f);
  
  }
