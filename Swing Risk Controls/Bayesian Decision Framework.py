import numpy as np
import pandas as pd
from scipy.stats import norm as norm_dist
import matplotlib.pyplot as plt

class BayesianAnalysis:
    def __init__(self, data, mu_range, mu_0, sigma_0):
        self.data = data
        self.mu_range = mu_range
        self.mu_0 = mu_0
        self.sigma_0 = sigma_0
        self.n = len(self.data)
        self.x_bar = np.mean(self.data)
        self.sigma = np.std(self.data)
        self.prior = norm_dist.pdf(self.mu_range, loc=self.mu_0, scale=self.sigma_0)
        self.likelihood = norm_dist.pdf(self.x_bar, loc=self.mu_range, scale=self.sigma/np.sqrt(self.n))
        self.posterior = self.prior * self.likelihood
        self.posterior /= np.trapz(self.posterior, self.mu_range)
        self.mu_post = np.trapz(self.mu_range * self.posterior, self.mu_range)
        self.sigma_post = np.sqrt(np.trapz((self.mu_range - self.mu_post)**2 * self.posterior, self.mu_range))

def plot_posterior(posterior):
    plt.plot(posterior.mu_range, posterior.posterior, color='blue')
    plt.fill_between(posterior.mu_range, posterior.posterior-posterior.sigma_post, posterior.posterior+posterior.sigma_post, color='gray')
    plt.title('Posterior Distribution')
    plt.xlabel('mu')
    plt.ylabel('Probability Density')
    plt.show()

data = np.array([1.2, 1.5, 1.8, 2.0, 2.5])
mu_0 = 2.0
sigma_0 = 0.5
mu_range = np.linspace(0, 4, 1000)

bayes = BayesianAnalysis(data, mu_range, mu_0, sigma_0)
plot_posterior(bayes)
