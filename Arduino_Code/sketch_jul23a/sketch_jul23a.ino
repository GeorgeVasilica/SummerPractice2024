// Definim variabilele pentru tensiune, curent și starea ON/OFF
#define voltagePin 3
#define relayPin 7
#define currentPin 9

float voltage = 0.0;
float current = 0.0;
bool isOn = false;
float timePython = 0.0;
unsigned long timeNow=0.0;
unsigned long timeNow1=0.0;


void setup() {
  // Inițializăm comunicarea serială
  Serial.begin(9600);

  // Inițializăm pinurile necesare (dacă este necesar)
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(voltagePin, OUTPUT);
  pinMode(currentPin, OUTPUT);
  pinMode(relayPin, OUTPUT);
  digitalWrite(relayPin, HIGH);

  TCCR2B = TCCR2B & 0b11111000| 0x01;  // Set prescaler to 1 (31.25 kHz PWM frequency)
  delay(1000);
  analogWrite(voltagePin, 0);
  analogWrite(currentPin, 0);

}

void loop() {
  // Verificăm dacă sunt disponibile date pe Serial
  if (Serial.available() > 0)
  {
    // Citim linia de date primită
    String data = Serial.readStringUntil('\n');
    // Împărțim datele primite în funcție de delimitatorul ' ' (spațiu)

    int firstSpace = data.indexOf(' ');
    int secondSpace = data.indexOf(' ', firstSpace + 1);
    int thirdSpace = data.indexOf(' ', secondSpace + 1);

    if (firstSpace > 0 && secondSpace > firstSpace && thirdSpace > secondSpace)
    {
      // Extragem tensiunea
      voltage = data.substring(0, firstSpace).toFloat();
      // Extragem curentul
      current = data.substring(firstSpace + 1, secondSpace).toFloat();
      // Extragem starea ON/OFF
      isOn = data.substring(secondSpace + 1, thirdSpace).toInt();
      //Extragem timpul
      timePython = data.substring(thirdSpace + 1).toFloat();
      digitalWrite(relayPin, HIGH);

      float voltageA=voltage/5.6;
      float PWM=voltageA*51;
      
      float currentA=current/18.9;
      float PWM_C=currentA*26;

      analogWrite(voltagePin,PWM);
      analogWrite(currentPin, PWM_C);

      if(timePython > 0.0){
        timeNow = millis() - timeNow1;
        if(timeNow > timePython){
          digitalWrite(relayPin,LOW);
        }
      }
      else{
        timeNow1 = millis();
      }

    }
  }
}
 