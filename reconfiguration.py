# PoC/sim/reconfigurator.py
import json
from prompt_adapter import PromptAdapter
from federated_meta_learning import FederatedMetaLearner
from simulator_interface import SimulatorInterface

class Reconfigurator:
    def __init__(self, prompt_schema_path):
        self.adapter = PromptAdapter(prompt_schema_path)
        self.meta = FederatedMetaLearner()
        self.sim = SimulatorInterface()

    def run_once(self, workload_prompt_path):
        prompt = self.adapter.load_prompt(workload_prompt_path)
        config_hint = self.adapter.decompose_to_config(prompt)
        adapted_config = self.meta.adapt(config_hint)
        self.sim.apply_configuration(adapted_config)
        return adapted_config

if __name__ == "__main__":
    rec = Reconfigurator("sim/prompt_schema.json")
    config = rec.run_once("sim/workload_prompts/industrial_iot.json")
    print("Applied config:", config)
