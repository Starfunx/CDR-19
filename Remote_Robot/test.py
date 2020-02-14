import numpy as np
import matplotlib.pyplot as plt

values = np.load("Values3.npy")

# affichage
fig, axs = plt.subplots(2, 1, sharex=True)
axs[0].plot(values[:,0])
axs[0].plot(values[:,4])
axs[0].set_ylabel('vitesse G (mm.s^-1)')
axs[0].grid(True)

axs[1].plot(values[:,2])
axs[1].set_xlabel('time (ech)')
axs[1].set_ylabel('commande G')
axs[1].grid(True)
fig.tight_layout()



fig2, axs2 = plt.subplots(2, 1, sharex=True)
axs2[0].plot(values[:,1])
axs2[0].plot(values[:,5])
axs2[0].set_ylabel('vitesse D (mm.s^-1)')
axs2[0].grid(True)

axs2[1].plot(values[:,3])
axs2[1].set_xlabel('time (ech)')
axs2[1].set_ylabel('commande D')
axs2[1].grid(True)
fig2.tight_layout()

plt.show()
