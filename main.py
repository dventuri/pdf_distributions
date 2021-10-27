import numpy as np
import matplotlib.pyplot as plt

# Normal distribution



# Log-normal
mu, sigma = 3, 1
s = np.random.lognormal(mu, sigma, 1000)

count, bins, ignored = plt.hist(s, 100, density=True, align='mid')

x = np.linspace(min(bins), max(bins), 10000)
pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))
    / (x * sigma * np.sqrt(2 * np.pi)))

plt.plot(x, pdf, linewidth=2, color='r')
plt.axis('tight')



# Rosin-Rammler



# Nukiyama-Tanasawa


