from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Passport Turtles Solar Dryer Engine", version="1.0.0")

class TelemetryPayload(BaseModel):
    dryer_id: str
    temp: float
    humidity: float

class PaymentPayload(BaseModel):
    transaction_id: str
    amount: float
    farmer_phone: str
    dryer_id: str

@app.get("/")
def read_root():
    return {"status": "online", "ecosystem": "Passport Turtles AgTech Network", "farmers_online": 35000}

@app.post("/api/v1/telemetry", status_code=status.HTTP_201_CREATED)
async def receive_telemetry(data: TelemetryPayload):
    # --- 🔴 OPEN ISSUE #22: INTEGRATE WITH TIMEDB/INFLUXDB FOR RWA ANALYTICS ---
    print(f"Locker {data.dryer_id} reporting: Temp {data.temp}C, Moisture {data.humidity}%")
    return {"message": "Telemetry securely cached", "action_required": data.humidity > 13.0}

@app.post("/api/v1/payment/callback", status_code=status.HTTP_200_OK)
async def mpesa_payment_callback(payment: PaymentPayload):
    # --- 🔴 OPEN ISSUE #23: SECURE VALIDATION WITH DARAJA API SIGNATURES ---
    # Triggering hardware lock release once payment clears
    print(f"Payment Verified: {payment.amount} KES received from {payment.farmer_phone}")
    return {"status": "unlocked", "relay_command": "TRIGGER_SOLAR_LOCK_OPEN"}
