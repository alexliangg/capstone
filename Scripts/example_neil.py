import pandas
import matplotlib.pyplot as plt


sample = pandas.read_csv("hustle_defense_overall.csv")
plt.figure()
plt.plot(sample['DEF_RIM_FG_PCT'])
plt.xlabel('player')
plt.ylabel('percentage')
pick_name = 'name.png'
plt.savefig(pick_name)

print('stop')

