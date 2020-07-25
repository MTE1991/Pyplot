# Source: https://corona.gov.bd/

import matplotlib.pyplot as plt 

dates = [18,19,20,21,22,23,24,25]
pos_cases = [2709,2459,2928,3057,2744,2856,2548,2520]
tests = [10923,10625,13362,12898,12050,12398,12027,10446]
deaths = [34,37,50,41,42,50,35,38]
fig, ax = plt.subplots(2)

fig.set_figheight(20)

ax[0].bar(dates, tests, width=0.5, label="No. of tests")
ax[0].bar(dates, pos_cases, width=0.5, label="Positive cases")

ax[0].set_title('COVID 19 scenario in BD (18-25 July, 2020)')
ax[0].legend()

ax[1].set_title("Reported Deaths")
ax[1].bar(dates, deaths, alpha=0.75, width=0.5, label="Deaths", color='c', edgecolor='r')
ax[1].set_ylabel("No. of deaths")

plt.show()
