// reading temperature from dht sensor
void read_temp()
{
  DHT dht(DHTPIN, DHTTYPE);
  dht.begin();
  extern float temp; 
  temp = dht.readTemperature();
}

// reading temperature from vibration sensor
void read_vibration()
{
  extern int vibr ;
  extern int maxi_vib;
  extern int mini_vib;
  vibr = pulseIn(vib,HIGH);
  vibr = map(vibr,0,1023,mini_vib,maxi_vib);
}

// reading temperature from gas sensor
void gas_sensor()
{
  extern int gas;
  extern int max_gas;
  extern int min_gas;
  gas = analogRead(gs);
  gas = map(gas,0,4095, min_gas, max_gas);
}

// ISR
int fl = HIGH;
void flame()
{
  fl = digitalRead(flames);
  if(fl == LOW)
  digitalWrite(alert,HIGH);
  else 
  digitalWrite(alert,LOW);
}

// data transfer indication
//void blinks()
//{
//  digitalWrite(LED_BUILTIN, 0);
//  delay(500);
//  digitalWrite(LED_BUILTIN, 1);
//  delay(100);
//}
