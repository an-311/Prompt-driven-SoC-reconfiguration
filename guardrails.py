# PoC/security/guardrails.py
def enforce_policy(config, attested=True):
    # very simple guard: require attestation before applying any config
    if not attested:
        return {"allow": False, "reason": "Attestation missing"}
    return {"allow": True}
