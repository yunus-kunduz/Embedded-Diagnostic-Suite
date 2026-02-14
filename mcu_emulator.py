import serial
import time
import struct
import numpy as np

# NOT: 'COM1' yerine com0com'da oluşturduğun port ismini yazmalısın
try:
    ser = serial.Serial('COM1', 115200)
    print("Sanal MCU Baslatildi: COM1 uzerinden veri gonderiliyor...")
except:
    print("HATA: COM1 bulunamadi. com0com ayarlarini kontrol edin.")
    exit()

while True:
    t = time.time()
    # 12-bit ADC (0-4095) simülasyonu + Gerçekçi Gürültü
    # Bu veri senin STM32 projerindeki potansiyometre verisini taklit eder
    raw_val = 2048 + 1000 * np.sin(t) + np.random.normal(0, 50)
    pot_val = int(np.clip(raw_val, 0, 4095))
    
    # Buton durumu (Her 5 saniyede bir 1 olur)
    btn_state = 1 if int(t) % 5 == 0 else 0
    
    # Veriyi Binary (İkili) formatta paketle (STM32 Struct yapısı gibi)
    # <HBB -> uint16 (ADC), uint8 (Buton), uint8 (Sayıcı)
    packet = struct.pack('<HBB', pot_val, btn_state, int(t) % 256)
    
    ser.write(packet)
    time.sleep(0.1) # 100ms periyot