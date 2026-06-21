# ☀️ passport-solar-dryer-core 🌾

License: MIT <br>
Campaign: #AfricaSpeaks

Welcome to the **passport-solar-dryer-core** repository. <br> 
This project serves as the smart, open-source embedded backbone for an automated solar food dehydration system. <br> 
By combining renewable thermal energy with low-power IoT monitoring, this system drastically minimizes agricultural post-harvest spoilage and preserves crop economic value.

---

## 📢 The #AfricaSpeaks Campaign

This repository is built in direct alignment with the **#AfricaSpeaks** initiative. 

Sub-Saharan smallholder farmers lose devastating percentages of their harvests due to inadequate preservation facilities. <br> 
We are shifting the narrative from passive aid to active engineering. <br> 
By open-sourcing localized agritech tools, we empower engineers, farmers, and innovators across Africa to build, modify, and deploy scalable solutions right in their home communities.

---

## ✨ Features & Functionality

*   **⚡ Smart Climate Actuation:** Automated ventilation and heat distribution logic triggered by internal environment thresholds.
*   **📊 Multi-Sensor Data Logging:** Real-time collection of temperature, ambient humidity, and moisture metrics.
*   **🔋 Off-Grid Ready:** Optimized for low-power operation on solar PV and battery setups.
*   **🔌 Extensible Architecture:** Modular framework designed to support ESP32, Arduino, and alternative microcontrollers.

---

## 🛠️ Hardware Ecosystem

The core firmware is built to interface seamlessly with:
*   **Microcontrollers:** ESP32 / Arduino platforms
*   **Sensors:** DHT22, SHT31, or analog soil/crop moisture probes
*   **Actuators:** 12V DC Fans, PWM speed controllers, or Solid State Relays (SSR)

---

## 🚀 Getting Started

### Prerequisites
*   [Arduino IDE](https://arduino.cc) or [PlatformIO](https://platformio.org)
*   Required sensor libraries (specified in the configuration file)

### Installation
1. Clone the repository to your local directory:
   ```bash
   git clone https://github.com
   ```
2. Navigate to the src directory and open the primary project configuration code.
3. Configure your pinouts, sensor types, and target temperature thresholds.
4. Flash the firmware to your microcontroller.

---

## 🤝 Contributing & Collaboration

We firmly believe that the best solutions are co-created. If you want to contribute:
1. Fork this project repository.
2. Form a new feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your updates (`git commit -m 'Add some AmazingFeature'`).
4. Push to your active branch (`git push origin feature/AmazingFeature`).
5. Open a formal Pull Request for code review.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for complete details.
