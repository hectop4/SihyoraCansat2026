#include <Wire.h>
#include <Adafruit_BMP085.h>

Adafruit_BMP085 bmp;

void setup()
{
  Serial.begin(115200);
  Wire.begin(18, 46); // SDA, SCL

  Serial.println("=== TEST BMP180 ===");

  if (!bmp.begin())
  {
    Serial.println("❌ Sensor BMP180 NO detectado");
    while (1)
      ;
  }

  Serial.println("✅ Sensor BMP180 OK");
}

void loop()
{
  Serial.print("Temperatura: ");
  Serial.print(bmp.readTemperature());
  Serial.println(" °C");

  Serial.print("Presión: ");
  Serial.print(bmp.readPressure());
  Serial.println(" Pa");

  Serial.print("Altitud: ");
  Serial.print(bmp.readAltitude());
  Serial.println(" m");

  Serial.println("----------------------");
  delay(2000);
}
