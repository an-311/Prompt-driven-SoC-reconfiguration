# PoC/ai_model/tiny_meta_learner.py
import numpy as np

class TinyMetaLearner:
    def __init__(self, n_priors=4):
        self.priors = np.ones(n_priors) / n_priors
        self.state = np.zeros(n_priors)

    def adapt(self, config_hint):
        # naive adaptation: update a prior based on workload_id
        wid = int(config_hint.get("workload_id", 0)) % len(self.priors)
        self.state[wid] += 1
        self.priors = (self.state + 1e-6) / (self.state.sum() + 1e-6 * len(self.priors))
        return {"selected_blocks": config_hint.get("blocks", ["NPU"]), "precision": config_hint.get("precision", "8bit")}
