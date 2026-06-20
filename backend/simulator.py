import time
import random
import requests

BACKEND_URL = "http://127.0.0"

print("🐢 PASSPORT TURTLES: Starting 24 Solar Crop Dryer Asset Simulation...")
print("Connecting virtual hardware matrix to local cloud development node...")

# Simulate 24 automated dryers deployed in the field
dryer_ids = [f"DRYER_SSA_{i:02d}" for i in range(1, 25)]

try:
    while True:
        selected_dryer = random.choice(dryer_ids)
        
        # Simulate normal drying vs a sudden humidity spike (e.g., rural rainstorm)
        if random.random() > 0.85:
            humidity = round(random.uniform(14.0, 22.0), 2)  # Critical spoilage surge
            print(f"\n⚠️ [WEATHER SYSTEM ALERT] Unexpected humidity surge detected at node {selected_dryer}!")
        else:
            humidity = round(random.uniform(8.5, 12.8), 2)   # Safe optimized drying range

        temperature = round(random.uniform(38.0, 48.0), 2)   # Solar thermal load (Celsius)

        # 1. Ship virtual hardware telemetry to FastAPI backend
        telemetry_data = {
            "dryer_id": selected_dryer,
            "temp": temperature,
            "humidity": humidity
        }
        
        try:
            res = requests.post(f"{BACKEND_URL}/telemetry", json=telemetry_data)
            if res.status_code == 201:
                action = "🔥 ACTIVATING SOLAR FANS (Flushing Rot Risk)" if humidity > 13.0 else "✅ STABLE"
                print(f"[{selected_dryer}] Telemetry Sent -> Temp: {temperature}°C | Humidity: {humidity}% | Hardware State: {action}")
        except requests.exceptions.ConnectionError:
            print("❌ Backend connection offline. Make sure 'uvicorn main:app' is running.")
            break

        # 2. Randomly simulate a farmer paying their pay-as-you-go drying utility fee via mobile money
        if random.random() > 0.90:
            payment_data = {
                "transaction_id": f"MPESA_TX_{random.randint(100000, 999999)}",
                "amount": 25.00, # 25 KES
                "farmer_phone": f"+254700{random.randint(100000, 999999)}",
                "dryer_id": selected_dryer
            }
            print(f"\n💰 [MOBILE MONEY INBOUND] Farmer processing pay-as-you-go micro-fee for {selected_dryer}...")
            pay_res = requests.post(f"{BACKEND_URL}/payment/callback", json=payment_data)
            print(f"📡 [GATEWAY RESPONSE] Webhook Trigger Result: {pay_res.json()}")

        time.sleep(2) # Run simulation clock tick every 2 seconds

except KeyboardInterrupt:
    print("\n🛑 Simulation terminated securely by core operator.")
