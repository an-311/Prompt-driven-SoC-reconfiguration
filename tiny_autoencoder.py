# PoC/ai_model/tiny_autoencoder.py
import numpy as np

class TinyAutoencoder:
    def __init__(self, input_dim=8, latent_dim=4):
        # tiny random seed for deterministic demo
        self.We = np.random.randn(input_dim, latent_dim) * 0.1
        self.Wd = np.random.randn(latent_dim, input_dim) * 0.1

    def reconstruct_error(self, x):
        z = x.dot(self.We)
        x_hat = z.dot(self.Wd)
        error = np.mean((x - x_hat) ** 2)
        return float(error)

