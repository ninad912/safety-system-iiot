#include "ESP_MICRO.h"
/* This code has been written for NodeMCU 1.0 (ESP 12 Module)*/
//int i=0, j=0, k=0;
float temp=0.0; 
int vibr = 0, maxi_vib =1000, mini_vib = 0;
int gas = 0, min_gas = 0, max_gas = 10000;

void setup(){
  Serial.begin(9600);
  start("IoT","1234567890");
    pinMode(vib, INPUT);
    pinMode(gs, INPUT);
    pinMode(flames, INPUT);
    pinMode(LED_BUILTIN,OUTPUT);
    pinMode(alert, OUTPUT);
    digitalWrite(LED_BUILTIN,HIGH);
  //attachInterrupt(digitalPinToInterrupt(flames), flame, RISING);    // fit an external LED inplace of built in LED.
}

void loop(){
  String post;
  read_temp();
  read_vibration();
  gas_sensor();
  flame();

  
//  //Broadcast test data
//  i = i+1;
//  j = j+2;
//  k = k+3;
//  post = post + String(i) + " ";
//  post = post + String(j) + " ";
//  post = post + String(k); 
  
  waitUntilNewReq();  
  post = post + String(vibr) + " ";
  post = post + String(gas) + " ";
  returnThisStr(post);
//  blinks();
}
