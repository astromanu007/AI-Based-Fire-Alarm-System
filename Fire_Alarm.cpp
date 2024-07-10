#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

const char* ssid = "your_SSID";
const char* password = "your_PASSWORD";

ESP8266WebServer server(80);

void setup() {
    Serial.begin(115200);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.println("Connecting...");
    }
    Serial.println("Connected!");

    pinMode(D1, OUTPUT);
    digitalWrite(D1, LOW);

    server.on("/light_on", [](){
        digitalWrite(D1, HIGH);
        server.send(200, "text/plain", "Light On");
    });

    server.on("/light_off", [](){
        digitalWrite(D1, LOW);
        server.send(200, "text/plain", "Light Off");
    });

    server.begin();
}

void loop() {
    server.handleClient();
}
