/*
====     Nota: Para el wifi utilizar una red que no sea 5G, preferiblemente compartan internet desde su celular       =====
====     y unanse a esa red desde el computador. Cuando ya  se haya compilado el código revisen el monitor serial     =====
====     de arduino y ahí les va a dar una ip, esa ip copienla en su buscador y ahí pueden tomar y ver las fotos      =====
====     de la cámara.                                                                                                =====
*/
#include "esp_camera.h"
#include <WiFi.h>

//  Cambia por el nombre y contraseña de tu red WiFi
const char *ssid = "------";
const char *password = "------";

// 🔧 Pines para la cámara OV2640 en ESP32-WROVER (Freenove)
#define PWDN_GPIO_NUM -1
#define RESET_GPIO_NUM -1
#define XCLK_GPIO_NUM 21
#define SIOD_GPIO_NUM 26
#define SIOC_GPIO_NUM 27

#define Y9_GPIO_NUM 35
#define Y8_GPIO_NUM 34
#define Y7_GPIO_NUM 39
#define Y6_GPIO_NUM 36
#define Y5_GPIO_NUM 19
#define Y4_GPIO_NUM 18
#define Y3_GPIO_NUM 5
#define Y2_GPIO_NUM 4
#define VSYNC_GPIO_NUM 25
#define HREF_GPIO_NUM 23
#define PCLK_GPIO_NUM 22

WiFiServer server(80);

void startCameraServer()
{
  server.begin();
  Serial.println("Servidor web iniciado");
}

void setup()
{
  Serial.begin(115200);
  delay(1000);

  //  Configuración de cámara
  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sscb_sda = SIOD_GPIO_NUM;
  config.pin_sscb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXFORMAT_JPEG;

  // 🔍 Frame size
  config.frame_size = FRAMESIZE_QVGA; // Puedes usar FRAMESIZE_VGA, FRAMESIZE_SVGA, etc.
  config.jpeg_quality = 10;
  config.fb_count = 1;

  //  Inicializar cámara
  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK)
  {
    Serial.printf("Error inicializando la cámara: 0x%x", err);
    return;
  }

  // 🌐 Conectar WiFi
  WiFi.begin(ssid, password);
  Serial.print("Conectando a WiFi...");
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi conectado");
  Serial.print("Dirección IP local: ");
  Serial.println(WiFi.localIP());

  startCameraServer();
}

void loop()
{
  WiFiClient client = server.available();
  if (!client)
    return;

  // Esperar petición
  while (!client.available())
    delay(1);
  String req = client.readStringUntil('\r');
  client.readStringUntil('\n');

  if (req.indexOf("/stream") != -1)
  {
    Serial.println("Iniciando stream...");
    client.println("HTTP/1.1 200 OK");
    client.println("Content-Type: multipart/x-mixed-replace; boundary=frame");
    client.println();

    while (client.connected())
    {
      camera_fb_t *fb = esp_camera_fb_get();
      if (!fb)
      {
        Serial.println("Error capturando imagen");
        break;
      }

      client.println("--frame");
      client.println("Content-Type: image/jpeg");
      client.printf("Content-Length: %u\n\n", fb->len);
      client.write(fb->buf, fb->len);
      client.println();
      esp_camera_fb_return(fb);
      delay(30);
    }
  }
  else
  {
    // Página HTML

    client.println("HTTP/1.1 200 OK");
    client.println("Content-Type: text/html\n");
    client.println("<!DOCTYPE html><html><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'>");
    client.println("<title>Webcam</title>");
    client.println("<style>");
    client.println("body{margin:0;background:#000;color:#f2f2f2;font-family:sans-serif;}header{text-align:center;padding:1rem;background:#111;}h1{margin:0;font-size:2rem;}main{display:flex;justify-content:center;gap:2rem;flex-wrap:wrap;padding:2rem;}.");
    client.println("camera-box{background:#1a1a1a;padding:1rem;border-radius:10px;flex:1 1 45%;}img{width:100%;max-width:1000px;border-radius:10px;border:2px solid #444;}.title{text-align:center;margin-bottom:1rem;font-weight:bold;font-size:1.2rem;}");
    client.println(".placeholder{width:100%;aspect-ratio:4/3;border:2px dashed #444;border-radius:10px;display:flex;align-items:center;justify-content:center;color:#777;font-style:italic;}");
    client.println("</style></head><body>");
    client.println("<header><h1>Webcam</h1></header><main>");
    client.println("<div class='camera-box'><div class='title'>Cámara 1</div><img src='/stream'></div>");
    client.println("<div class='camera-box'><div class='title'>Cámara 2</div><div class='placeholder'>Cámara aún no conectada</div></div>");
    client.println("</main></body></html>");
  }

  delay(1);
  client.stop();
  Serial.println("Cliente desconectado");
}
