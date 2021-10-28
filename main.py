import numpy as np
from numpy.lib.scimath import sqrt
import scipy.special as sps
import matplotlib.pyplot as plt


mu, sigma = 100, 15
s = np.random.normal(mu, sigma, 1000)

plt.figure()
n, bins, patches = plt.hist(s, 50, density=True, facecolor='g', alpha=0.75)
plt.xlabel('Diameters')
plt.ylabel('Probability')
plt.title('Histogram of Droplets')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.xlim(40, 160)
plt.ylim(0, 0.03)
plt.grid(True)


x = np.linspace(min(bins), max(bins), 10000)

# Normal distribution
pdf = (np.exp(-(x - mu)**2 / (2 * sigma**2))
    / (sigma*np.sqrt(2 * np.pi)))
plt.plot(x, pdf, linewidth=2, color='r')


# Log-normal
sigma_log = np.sqrt(np.log((sigma/mu)**2 + 1))
mu_log = np.log(mu) - sigma_log**2/2
pdf = (np.exp(-(np.log(x) - mu_log)**2 / (2 * sigma_log**2))
    / (x*sigma_log*np.sqrt(2*np.pi)))
plt.plot(x, pdf, linewidth=2, color='b')


# Rosin-Rammler
# pdf = 1. - np.exp(-(x/delta)**n)


# Nukiyama-Tanasawa



