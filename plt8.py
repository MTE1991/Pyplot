import matplotlib.pyplot as plt

# Source: https://corona.gov.bd/
dates = [1,2,3,4,5,6,7,8]
pos_cases = [2772,2960,3009,2695,2772,2199,886,1356]
tests = [12859,12714,14127,12937,12614,8802,3684,4249]
deaths = [37,35,35,48,28,21,22,30]

fig, ax = plt.subplots(2)
fig.set_figheight(10)

ax[0].set_title('COVID 19 scenario in BD')
ax[0].bar(dates, tests, width=0.5, label="No. of tests")
ax[0].bar(dates, pos_cases, width=0.5, label="Positive cases")
ax[0].set_xticks([1,2,3,4,5,6,7,8])
ax[0].set_xticklabels(['27 July','28 July','29 July','30 July','31 July','1 August','2 August','3 August'])
ax[0].legend()

ax[1].set_title("Reported Deaths")
ax[1].bar(dates, deaths, alpha=0.75, width=0.5, label="Deaths", color='r')
ax[1].set_ylabel("No. of deaths")
ax[1].set_xticks([1,2,3,4,5,6,7,8])
ax[1].set_xticklabels(['27 July','28 July','29 July','30 July','31 July','1 August','2 August','3 August'])

plt.show()