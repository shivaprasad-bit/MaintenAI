import random

class DigitalMotor:
    def __init__(self):
        self.temperature = 40.0
        self.wear = 0.0
        self.rpm = 1500
        self.voltage = 230

    def generate_sensor_data(self):
        load = random.uniform(0.4, 1.0)
        self.wear += random.uniform(0.02, 0.08)
        self.temperature += (load * 1.5) - random.uniform(0.2, 0.8)

        vibration = 0.2 + (self.wear * 0.02) + random.uniform(-0.03, 0.03)
        rpm = self.rpm + random.randint(-5, 5)
        voltage = self.voltage + random.uniform(-2, 2)
        health = max(0, round(100 - self.wear))

        return {
            "temperature": round(self.temperature, 1),
            "vibration": round(vibration, 2),
            "rpm": rpm,
            "voltage": round(voltage, 1),
            "health": health
        }

motor = DigitalMotor()