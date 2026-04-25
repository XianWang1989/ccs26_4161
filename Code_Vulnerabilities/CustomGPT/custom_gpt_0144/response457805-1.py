import matplotlib.pyplot as plt

event_index = ['event 1','event 2','event 3','event 4','event 5','event 6','event 7','event 8','event 9','event 10']
x = list(range(1, len(event_index)+1))

list1 = [0.7,0.8,0.8,0.9,0.8,0.7,0.6,0.9,1.0,0.9]
list2 = [0.2,0.3,0.1,0.0,0.2,0.1,0.3,0.1,0.2,0.1]
list3 = [0.4,0.6,0.4,0.5,0.4,0.5,0.6,0.4,0.5,0.4]
list4 = [78,87,77,65,89,98,74,94,85,73]
list5 = [16,44,14,55,34,36,76,54,43,32]

fig, (ax1, ax3) = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

# Subplot 1
ax2 = ax1.twinx()
line1 = ax1.plot(x, list1, 'bo-', label='list1')
line2 = ax1.plot(x, list2, 'go-', label='list2')
line3 = ax1.plot(x, list3, 'ro-', label='list3')
line4 = ax2.plot(x, list4, 'yo-', label='list4')

ax1.set_ylim(0, 1)
ax2.set_ylim(0, 100)
ax1.set_ylabel('Some values', fontsize=12)
ax2.set_ylabel('% values', fontsize=12)

# Subplot 2
line5 = ax3.plot(x, list5, 'mo-', label='list5')
ax3.plot(x, list4, 'yo-', label='list4')
ax3.set_ylim(0, 100)
ax3.set_ylabel('% values', fontsize=12)
ax3.set_xlabel('Events')
ax3.set_xticks(x)
ax3.set_xticklabels(event_index, rotation=45)
ax3.tick_params(axis='y', which='both', left=False, right=False, labelleft=False)

# Legend
lines = line1 + line2 + line3 + line4 + line5
labels = [l.get_label() for l in lines]
fig.legend(lines, labels, loc='lower center', ncol=5, bbox_to_anchor=(0.5, -0.05))

# Titles
fig.suptitle('Some trends', y=1.02, fontsize=17)
fig.text(0.5, 0.94, 'Upper panel: list 1, 2, 3, and 4 | Lower panel: list 4 and 5',
         ha='center', fontsize=9)

fig.tight_layout(rect=[0, 0.05, 1, 0.93])
plt.show()
