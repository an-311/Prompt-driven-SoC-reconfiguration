# PoC/tests/test_scenarios.py
def test_prompt_mapping():
    from PoC.sim.prompt_adapter import PromptAdapter
    adapter = PromptAdapter("PoC/data/prompts_schema.json")
    prompt = {"enabled_blocks": ["NPU"], "memory_partition": "per-block", "precision": "8bit", "workload_id": 2}
    cfg = adapter.decompose_to_config(prompt)
    assert "blocks" in cfg

def test_sim_run():
    from PoC.sim.simulator_interface import SimulatorInterface
    sim = SimulatorInterface()
    sim.apply_configuration({"blocks": ["NPU"], "memory": "per-block", "precision": "8bit"})
    assert sim.current_config["blocks"] == ["NPU"]
