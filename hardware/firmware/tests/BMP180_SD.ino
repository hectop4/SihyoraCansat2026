#include <SPI.h>
#include <SD.h>
#include <Wire.h>
#include <Adafruit_BMP085.h>

// ---------- CONFIGURACIÓN ----------
#define PIN_SD_CS 10 // CS de la microSD
#define I2C_SDA 8    // SDA ESP32-S3
#define I2C_SCL 9    // SCL ESP32-S3

File archivo;
Adafruit_BMP085 bmp;
float altitud_base = 0.0;

// ---------- SETUP ----------
void setup()
{
  Serial.begin(115200);
  delay(1000);

  Serial.println("=== Registro BMP180 en SD ===");

  // ---- I2C ----
  Wire.begin(I2C_SDA, I2C_SCL);

  if (!bmp.begin())
  {
    Serial.println("Error: BMP180 no detectado");
    while (1)
      ;
  }
  Serial.println("BMP180 OK");
  delay(2000); // tiempo para estabilizar el sensor

  altitud_base = bmp.readAltitude(101325);

  Serial.print("Altura base fijada en: ");
  Serial.print(altitud_base);
  Serial.println(" m (referencia 0)");

  // ---- SD ----
  if (!SD.begin(PIN_SD_CS))
  {
    Serial.println(" Error módulo SD");
    ESP.restart();
  }
  Serial.println("Módulo SD inicializado");

  // ---- Crear archivo ----
  archivo = SD.open("/registros.csv", FILE_WRITE);
  if (!archivo)
  {
    Serial.println(" Error al crear archivo");
    while (1)
      ;
  }

  archivo.println("Temperatura_C,Presion_Pa,Altitud_m");
  archivo.close();

  Serial.println("Archivo listo");
}

// ---------- LOOP ----------
void loop()
{
  float temperatura = bmp.readTemperature();
  long presion = bmp.readPressure();
  float altitud_actual = bmp.readAltitude(101325);
  float altitud = altitud_actual - altitud_base;

  Serial.print("T: ");
  Serial.print(temperatura);
  Serial.print(" °C | P: ");
  Serial.print(presion);
  Serial.print(" Pa | A: ");
  Serial.print(altitud);
  Serial.println(" m");

  archivo = SD.open("/registros.csv", FILE_APPEND);
  if (archivo)
  {
    archivo.print(temperatura);
    archivo.print(",");
    archivo.print(presion);
    archivo.print(",");
    archivo.println(altitud);
    archivo.close();
  }
  else
  {
    Serial.println(" Error al escribir en SD");
  }

  delay(2000);
}
