import numpy as np
import pandas as pd
from scipy.stats import norm as norm_dist
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

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

def run_bayesian_analysis(data, mu_0, sigma_0, mu_range):
    bayes = BayesianAnalysis(data, mu_range, mu_0, sigma_0)
    return bayes

def on_calculate():
    # Get input values
    data = np.array([float(x) for x in data_entry.get().split(',')])
    mu_0 = float(mu_0_entry.get())
    sigma_0 = float(sigma_0_entry.get())
    mu_min = float(mu_min_entry.get())
    mu_max = float(mu_max_entry.get())
    n_points = int(n_points_entry.get())
    mu_range = np.linspace(mu_min, mu_max, n_points)

    # Run Bayesian analysis
    bayes = run_bayesian_analysis(data, mu_0, sigma_0, mu_range)

    # Update output labels
    mu_post_label.config(text='mu_post = {:.2f}'.format(bayes.mu_post))
    sigma_post_label.config(text='sigma_post = {:.2f}'.format(bayes.sigma_post))

    # Plot posterior distribution
    plot_posterior(bayes)

# Create GUI
root = tk.Tk()
root.title('Bayesian Analysis')
root.geometry('400x300')

# Data input
data_label = ttk.Label(root, text='Data:')
data_label.pack()
data_entry = ttk.Entry(root)
data_entry.pack()
data_entry.insert(0, '1.2, 1.5, 1.8, 2.0, 2.5')

# Prior input
prior_label = ttk.Label(root, text='Prior:')
prior_label.pack()
prior_frame = ttk.Frame(root)
prior_frame.pack()
mu_0_label = ttk.Label(prior_frame, text='mu_0:')
mu_0_label.grid(row=0, column=0)
mu_0_entry = ttk.Entry(prior_frame, width=10)
mu_0_entry.grid(row=0, column=1)
mu_0_entry.insert(0, '2.0')
sigma_0_label = ttk.Label(prior_frame, text='sigma_0:')
sigma_0_label.grid(row=1, column=0)
sigma_0_entry = ttk.Entry(prior_frame, width=10)
sigma_0_entry.grid(row=1, column=1)
sigma_0_entry.insert(0, '0.5')

range_label = ttk.Label(root, text='Range:')
range_label.pack()
range_frame = ttk.Frame(root)
range_frame.pack()
mu_min_label = ttk.Label(range_frame, text='mu_min:')
mu_min_label.grid(row=0, column=0)
mu_min_entry = ttk.Entry(range_frame, width=10)
mu_min_entry.grid(row=0, column=1)
mu_min_entry.insert(0, '0')
mu_max_label = ttk.Label(range_frame, text='mu_max:')
mu_max_label.grid(row=1, column=0)
mu_max_entry = ttk.Entry(range_frame, width=10)
mu_max_entry.grid(row=1, column=1)
mu_max_entry.insert(0, '4')
n_points_label = ttk.Label(range_frame, text='n_points:')
n_points_label.grid(row=2, column=0)
n_points_entry = ttk.Entry(range_frame, width=10)
n_points_entry.grid(row=2, column=1)
n_points_entry.insert(0, '1000')

calculate_button = ttk.Button(root, text='Calculate', command=on_calculate)
calculate_button.pack()

output_label = ttk.Label(root, text='Output:')
output_label.pack()
mu_post_label = ttk.Label(root, text='mu_post = ')
mu_post_label.pack()
sigma_post_label = ttk.Label(root, text='sigma_post = ')
sigma_post_label.pack()

root.mainloop()