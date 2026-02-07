# PoC/sim/simulator_interface.py
class SimulatorInterface:
    def __init__(self):
        self.current_config = None

    def apply_configuration(self, config):
        self.current_config = config
        print(f"[SIM] Applied configuration: {config}")
        # Extend: return simulated latency and energy proxy
