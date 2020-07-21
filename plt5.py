import matplotlib.pyplot as plt
import numpy as np

langs = ('Python', 'C', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(langs))
tiobe_ratings = [9.09,16.45,6.21,15.1,.87,.31,.36]

plt.title('TIOBE Index for July 2020')
plt.bar(y_pos, tiobe_ratings, align='center', alpha=0.8)
plt.xticks(y_pos, langs)
plt.ylabel('TIOBE Rating (%)')

plt.show()