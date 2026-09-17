import serial
import threading
import webview
import time
import sys

ARDUINO_PORT = "COM12" 
BAUD_RATE = 9600

# Pencerenin 1 kez açılmasını kontrol eden değişken
pencere_acildi = False
pencere_nesnesi = None

def arduino_dinle():
    global pencere_acildi
    
    try:
        ser = serial.Serial(ARDUINO_PORT, BAUD_RATE, timeout=1)
        print(f"[OK] {ARDUINO_PORT} dinleniyor...")

        while True:
            if ser.in_waiting > 0:
                veri = ser.readline().decode('utf-8', errors='ignore').strip()
                
                if veri == "TETIKLE" and not pencere_acildi:
                    pencere_acildi = True
                    print("[TETIKLENDI] HTML penceresi aciliyor...")
                    
                    # Ana thread'de duran pencereyi gösteriyoruz
                    if pencere_nesnesi:
                        pencere_nesnesi.show()
                        
                elif veri == "TETIKLE" and pencere_acildi:
                    print("[ENGELLENDI] Pencere zaten 1 kez acildi.")
                    
            time.sleep(0.1)

    except Exception as e:
        print(f"[HATA] Seri port baglanti hatasi: {e}")

if __name__ == "__main__":
    # 1. HTML Penceresini Hazırla (Başlangıçta gizli tutuyoruz)
    dosya_yolu = r'C:\Users\user\OneDrive\Belgeler\afootbal kayıtları\trtrftb3.html'
    
    pencere_nesnesi = webview.create_window(
        'AFOOTBAL Paneli', 
        dosya_yolu, 
        width=1024, 
        height=768,
        hidden=True  # Tetiklenme gelene kadar gizli kalır
    )

    # 2. Arduino Dinleyiciyi Arka Plan Thread'ine Al
    t = threading.Thread(target=arduino_dinle, daemon=True)
    t.start()

    # 3. pywebview'ı Ana Thread Üzerinde Başlat
    webview.start()