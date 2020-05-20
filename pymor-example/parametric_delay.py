#!/usr/bin/env python
# coding: utf-8
#This file is part of the pyMOR project (http://www.pymor.org).
#Copyright 2013-2020 pyMOR developers and contributors. All rights reserved.
#License: BSD 2-Clause License (http://opensource.org/licenses/BSD-2-Clause)
# In[ ]:


import numpy as np
import scipy.linalg as spla
import matplotlib as mpl
import matplotlib.pyplot as plt

from pymor.basic import *


# # Model

# In[ ]:


def H(s, mu):
    tau = mu['tau']
    return np.array([[np.exp(-s) / (tau * s + 1)]])

def dH(s, mu):
    tau = mu['tau']
    return np.array([[-(tau * s + tau + 1) * np.exp(-s) / (tau * s + 1) ** 2]])


# In[ ]:


f = ProjectionParameterFunctional('tau', ())
parameter_space = CubicParameterSpace(f.parameter_type, 0.01, 1)

fom = TransferFunction(NumpyVectorSpace(1), NumpyVectorSpace(1),
                       H, dH,
                       parameter_space=parameter_space)


# # Magnitude plot

# In[ ]:


mu_list_short = [0.01, 0.1, 1]


# In[ ]:


w = np.logspace(-2, 4, 100)

fig, ax = plt.subplots()
for mu in mu_list_short:
    fom.mag_plot(w, ax=ax, mu=mu, label=fr'$\tau = {mu}$')
ax.legend()
#plot.sho()


# In[ ]:


w_list = np.logspace(-2, 4, 100)
mu_list = np.logspace(-2, 0, 50)

fom_w_mu = np.zeros((len(w_list), len(mu_list)))
for i, mu in enumerate(mu_list):
    fom_w_mu[:, i] = spla.norm(fom.freq_resp(w_list, mu=mu), axis=(1, 2))


# In[ ]:


fig, ax = plt.subplots()
out = ax.contourf(w_list, mu_list, fom_w_mu.T,
                  norm=mpl.colors.LogNorm(),
                  levels=np.logspace(np.log10(fom_w_mu.min()), np.log10(fom_w_mu.max()), 100))
ax.set_xlabel(r'Frequency $\omega$')
ax.set_ylabel(r'Parameter $\mu$')
ax.set_xscale('log')
ax.set_yscale('log')
fig.colorbar(out, ticks=np.logspace(-4, 1, 6))
#plot.sho()


# # TF-IRKA

# In[ ]:


r = 10
roms_tf_irka = []
for mu in mu_list_short:
    tf_irka = TFIRKAReductor(fom, mu=mu)
    rom = tf_irka.reduce(r, conv_crit='h2', maxit=1000, num_prev=5)
    roms_tf_irka.append(rom)


# In[ ]:


fig, ax = plt.subplots()
for mu, rom in zip(mu_list_short, roms_tf_irka):
    poles = rom.poles()
    ax.plot(poles.real, poles.imag, '.', label=fr'$\tau = {mu}$')
ax.set_title("Poles of TF-IRKA's ROMs")
ax.legend()
#plot.sho()


# In[ ]:


fig, ax = plt.subplots()
for mu, rom in zip(mu_list_short, roms_tf_irka):
    rom.mag_plot(w, ax=ax, label=fr'$\tau = {mu}$')
ax.set_title("Magnitude plot of TF-IRKA's ROMs")
ax.legend()
#plot.sho()


# In[ ]:


fig, ax = plt.subplots()
for mu, rom in zip(mu_list_short, roms_tf_irka):
    (fom - rom).mag_plot(w, ax=ax, mu=mu, label=fr'$\tau = {mu}$')
ax.set_title("Magnitude plot of error systems")
ax.legend()
#plot.sho()

