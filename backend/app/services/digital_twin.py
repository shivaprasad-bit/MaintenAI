import random
from datetime import datetime
from collections import deque


class DigitalMotor:
    def __init__(self):
        self.temperature = 40.0
        self.wear = 0.0
        self.rpm = 1500
        self.voltage = 230

        # Store last 100 sensor readings
        self.history = deque(maxlen=100)

    def generate_sensor_data(self):
        # Simulate machine load
        load = random.uniform(0.4, 1.0)

        # Wear increases gradually
        self.wear += random.uniform(0.05, 0.15)

        # Temperature changes realistically
        self.temperature += (load * 2) - random.uniform(0.3, 0.8)

        # Vibration increases with wear
        vibration = 0.2 + (self.wear * 0.03) + random.uniform(-0.02, 0.02)

        # RPM fluctuates slightly
        rpm = self.rpm + random.randint(-8, 8)

        # Voltage fluctuates slightly
        voltage = self.voltage + random.uniform(-3, 3)

        # Health decreases as wear increases
        health = max(0, round(100 - self.wear))

        # Determine machine state
        if health >= 80:
            status = "Healthy"
            recommendation = "No maintenance required."
        elif health >= 50:
            status = "Warning"
            recommendation = "Schedule maintenance soon."
        else:
            status = "Critical"
            recommendation = "Inspect motor bearings immediately."

        # Calculate failure probability
        failure_probability = min(99, round(100 - health + vibration * 10))

        # Create sensor reading
        reading = {
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "temperature": round(self.temperature, 1),
            "vibration": round(vibration, 2),
            "rpm": rpm,
            "voltage": round(voltage, 1),
            "health": health,
            "status": status,
            "failure_probability": failure_probability,
            "recommendation": recommendation
        }

        # Save to history
        self.history.append(reading)

        return reading

    def get_history(self):
        return list(self.history)


# Shared Digital Twin instance
motor = DigitalMotor()