import serial
import struct
import matplotlib.pyplot as plt
from collections import deque

class DiagnosticSuite:
    def __init__(self, port, baud=115200):
        self.ser = serial.Serial(port, baud, timeout=1)
        self.alpha = 0.40
        self.last_filtered = 0
        
        # Grafik için veri havuzları (Son 100 veri)
        self.raw_data = deque(maxlen=100)
        self.filtered_data = deque(maxlen=100)

    def low_pass_filter(self, current_val):
        filtered = (self.alpha * current_val) + (1 - self.alpha) * self.last_filtered
        self.last_filtered = filtered
        return filtered

    def run_with_plot(self):
        plt.ion() # İnteraktif mod açık
        fig, ax = plt.subplots()
        line_raw, = ax.plot([], [], 'r-', label='HAM (Gürültülü)', alpha=0.5)
        line_filt, = ax.plot([], [], 'b-', label='FILTRE (Pürüzsüz)', linewidth=2)
        ax.legend()
        ax.set_ylim(0, 4095) # STM32 12-bit ADC aralığı
        
        print(f"Analiz Sistemi Dinliyor: {self.ser.port}...")
        
        try:
            while True:
                data = self.ser.read(4)
                if len(data) == 4:
                    adc_raw, btn, cnt = struct.unpack('<HBB', data)
                    adc_filtered = self.low_pass_filter(adc_raw)
                    
                    # Verileri kuyruğa ekle
                    self.raw_data.append(adc_raw)
                    self.filtered_data.append(adc_filtered)
                    
                    # Grafiği güncelle
                    line_raw.set_data(range(len(self.raw_data)), list(self.raw_data))
                    line_filt.set_data(range(len(self.filtered_data)), list(self.filtered_data))
                    ax.set_xlim(0, 100)
                    
                    plt.pause(0.01)
                    print(f"Syc: {cnt:03d} | HAM: {adc_raw:4d} | FILTRE: {adc_filtered:6.1f}")
        except KeyboardInterrupt:
            print("\nSistem Durduruldu.")
            self.ser.close()

if __name__ == "__main__":
    DiagnosticSuite('COM2').run_with_plot()