import random

class DigitalMotor:
    def __init__(self):
        self.temperature = 40.0
        self.wear = 0.0
        self.rpm = 1500
        self.voltage = 230

    def generate_sensor_data(self):
        # Simulate machine load
        load = random.uniform(0.4, 1.0)

        # Wear increases gradually
        self.wear += random.uniform(0.05, 0.15)

        # Temperature changes realistically
        self.temperature += (load * 2) - random.uniform(0.3, 0.8)

        # Vibration grows with wear
        vibration = 0.2 + (self.wear * 0.03) + random.uniform(-0.02, 0.02)

        # RPM fluctuates slightly
        rpm = self.rpm + random.randint(-8, 8)

        # Voltage fluctuates slightly
        voltage = self.voltage + random.uniform(-3, 3)

        # Health decreases
        health = max(0, round(100 - self.wear))

        # Machine state
        if health >= 80:
            status = "Healthy"
            recommendation = "No maintenance required."
        elif health >= 50:
            status = "Warning"
            recommendation = "Schedule maintenance soon."
        else:
            status = "Critical"
            recommendation = "Inspect motor bearings immediately."

        # Failure probability
        failure_probability = min(99, round(100 - health + vibration * 10))

        return {
            "temperature": round(self.temperature, 1),
            "vibration": round(vibration, 2),
            "rpm": rpm,
            "voltage": round(voltage, 1),
            "health": health,
            "status": status,
            "failure_probability": failure_probability,
            "recommendation": recommendation
        }

# Create one shared Digital Motor instance
motor = DigitalMotor()