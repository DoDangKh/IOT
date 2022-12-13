#include<ESP8266WiFi.h>
#include<FirebaseESP8266.h>
#define  ssid "khoa's Galaxy A51"
#define  pass "fmja7355"
#define  firebaseid "arduino-1e690"
#define FIREBASE_HOST "arduino-1e690-default-rtdb.firebaseio.com"
#define FIREBASE_AUTH "xt7r6NGdHYtvznyZBFkw0BXOfZtCgz2LdukqF1Nm"

int cambien = D8;
String path="/";
FirebaseData f;
int giatriamthanh;
int giatribui;
int samplingtime=280;
int deltatime=40;
int sleeptime=9680;
float voMeasured=0;
float calcVoltage=0;
float dustDensity=0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(LED_BUILTIN,OUTPUT);
  //pinMode(cambien, INPUT);
  WiFi.begin(ssid,pass);
  WiFi.mode(WIFI_STA);
  Serial.print("Connecting to");
  Serial.print(ssid);
  while(WiFi.status() != WL_CONNECTED){
    Serial.print(".");
    delay(500);
  }
  Serial.println();
  Serial.print("Connected");
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  Firebase.reconnectWiFi(true);
  if(!Firebase.beginStream(f, path))
  {
      Serial.println("REASON: "+ f.errorReason());
      Serial.println();
  }
  pinMode(D8,OUTPUT);
  pinMode(D7,OUTPUT);//5v
  pinMode(D4,OUTPUT);//led
  digitalWrite(D8,HIGH);
} 

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(D8,HIGH);
    delay(100);
  giatriamthanh= analogRead(A0);
  
  //firebase.setInt("SOUND",giatri);
  digitalWrite(D8,LOW);
  delay(100);

  digitalWrite(D8,LOW);
  digitalWrite(D7,HIGH);
  delay(100);
  digitalWrite(D4,LOW);
  delayMicroseconds(samplingtime);

  voMeasured=analogRead(A0);
  delayMicroseconds(deltatime);
  digitalWrite(D4,HIGH);
  delayMicroseconds(sleeptime);
  calcVoltage = voMeasured *(5.0/1024.0);
  dustDensity= 170 * calcVoltage -0.1;
  giatribui=dustDensity;
  
  Serial.print("bui:") ;
  Serial.print(giatribui);
  Serial.print(" amthanh:");
  Serial.println(giatriamthanh);
  Firebase.setInt(f,path + "/SOUND", giatriamthanh);
  Firebase.setInt(f,path + "/DUST", giatribui);
  digitalWrite(D7,LOW);
  delay(100);
}