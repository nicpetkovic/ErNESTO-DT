from src.digital_twin.battery_models.generic_models import ThermalModel


class DummyThermal(ThermalModel):
    """
    The Dummy Thermal model simply simulates the temperature of the battery by copying the ground temperature.
    NOTE: this model cannot be employed to generate new data (what-if simulation)
    """
    def __init__(self, **kwargs):
        super().__init__(name='dummy_thermal')
        if 'ground_temps' in kwargs:
            self._ground_temps = kwargs['ground_temps']
        else:
            raise AttributeError("The parameter to initialize the attribute of DummyThermal has not benn passed!")

    @property
    def temps(self):
        return self._ground_temps

    def reset_model(self, **kwargs):
        self._temp_series = []

    def init_model(self, **kwargs):
        """
        Initialize the model at timestep t=0 with an initial temperature equal to 25 degC (ambient temperature)
        """
        temp = kwargs['temperature'] if 'temperature' in kwargs else 298.15
        heat = kwargs['dissipated_heat'] if 'dissipated_heat' in kwargs else 0

        self.update_temp(temp)
        self.update_heat(heat)

    def compute_temp(self, **kwargs):
        return self._ground_temps[kwargs['k']]