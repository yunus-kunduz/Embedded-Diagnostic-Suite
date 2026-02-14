# Embedded Diagnostic Suite & HIL Simulator

Bu proje, fiziksel bir STM32 kartı olmadan, Python üzerinden **Hardware-in-the-Loop (HIL)** simülasyonu gerçekleştirmek için tasarlanmıştır. 

## 🚀 Özellikler
* **Sanal MCU Emülatörü:** COM portu üzerinden gürültülü sensör verisi üretir.
* **Dijital Sinyal İşleme (DSP):** Gerçek zamanlı Alçak Geçiren Filtre (Low Pass Filter) uygular.
* **Canlı Görselleştirme:** Matplotlib ile ham ve filtrelenmiş verileri anlık grafikler.

## 📊 Matematiksel Model
Kullanılan filtre denklemi:
$$y[n] = \alpha \cdot x[n] + (1 - \alpha) \cdot y[n-1]$$

## 🛠 Kurulum
1. VSPE ile COM1-COM2 köprüsü kurun.
2. `pip install -r requirements.txt`
3. Önce `mcu_emulator.py`, ardından `diagnostic_suite.py` çalıştırın.

---