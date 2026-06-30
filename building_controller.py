class BuildingController:
    """
    Simulates the current state of the building.
    """

    def __init__(self):
        self.reset()

    def reset(self):
        self.lights = False
        self.temperature = 21
        self.doors_locked = True
        self.cameras_recording = True

    def turn_on_lights(self):
        self.lights = True

    def turn_off_lights(self):
        self.lights = False

    def set_temperature(self, temp):
        self.temperature = temp

    def unlock_doors(self):
        self.doors_locked = False

    def lock_doors(self):
        self.doors_locked = True

    def status(self):
        return {
            "lights": "ON" if self.lights else "OFF",
            "temperature": self.temperature,
            "doors": "Locked" if self.doors_locked else "Unlocked",
            "cameras": "Recording" if self.cameras_recording else "Offline"
        }