# PoC/sim/prompt_adapter.py
import json

class PromptAdapter:
    def __init__(self, schema_path):
        with open(schema_path, "r") as f:
            self.schema = json.load(f)

    def load_prompt(self, path):
        with open(path, "r") as f:
            return json.load(f)

    def decompose_to_config(self, prompt):
        blocks = prompt.get("enabled_blocks", ["NPU"])
        memory = prompt.get("memory_partition", "shared")
        precision = prompt.get("precision", "8bit")
        return {"blocks": blocks, "memory": memory, "precision": precision, "workload_id": prompt.get("workload_id", 0)}
