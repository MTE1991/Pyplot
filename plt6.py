# source : https://corona.gov.bd/

import matplotlib.pyplot as plt

fig, ax = plt.subplots(2)

fig.suptitle("COVID 19 scenario in BD (16-22 July, 2020)")
ax[0].set_title("Positive cases")
ax[0].plot([16,17,18,19,20,21,22],
[2733,3034,2709,2459,2928,3057,2744],'tab:red')

ax[1].set_title("Number of tests")
ax[1].plot([16,17,18,19,20,21,22],
[12889,13460,10923,10625,13362,12898,12050])

plt.show()
