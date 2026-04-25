
import matplotlib.pyplot as plt

event_index = ['event 1', 'event 2', 'event 3', 'event 4', 'event 5', 
               'event 6', 'event 7', 'event 8', 'event 9', 'event 10']
list1 = [0.7, 0.8, 0.8, 0.9, 0.8, 0.7, 0.6, 0.9, 1.0, 0.9]
list2 = [0.2, 0.3, 0.1, 0.0, 0.2, 0.1, 0.3, 0.1, 0.2, 0.1]
list3 = [0.4, 0.6, 0.4, 0.5, 0.4, 0.5, 0.6, 0.4, 0.5, 0.4]
list4 = [78, 87, 77, 65, 89, 98, 74, 94, 85, 73]
list5 = [16, 44, 14, 55, 34, 36, 76, 54, 43, 32]

fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(211)
ax2 = ax1.twinx()

ax1.plot(range(len(list1)), list1, 'bo-', label='list1')
ax1.plot(range(len(list2)), list2, 'go-', label='list2')
ax1.plot(range(len(list3)), list3, 'ro-', label='list3')
ax2.plot(range(len(list4)), list4, 'yo-', label='list4')

ax1.set_ylim(0, 1)
ax1.set_ylabel('Some values', fontsize=12)
ax2.set_ylabel('% values', fontsize=12)
ax2.set_ylim(0, 100)

ax3 = fig.add_subplot(212)
ax3.plot(range(len(list4)), list4, 'yo-', label='list4')
ax3.plot(range(len(list5)), list5, 'mo-', label='list5')

ax3.set_ylabel('% values', fontsize=12)
ax3.set_xlabel('events')
ax3.set_xticks(range(len(event_index)))
ax3.set_xticklabels(event_index)
ax3.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2)

title_string = 'Some trends'
subtitle_string = 'Upper panel: list 1, 2, 3, and 4 | Lower panel: list 4 and 5'
plt.suptitle(title_string, y=0.95, fontsize=17)
plt.figtext(0.5, 0.92, subtitle_string, ha='center', fontsize=8)

fig.tight_layout()
plt.subplots_adjust(top=0.88, bottom=0.2)
plt.show()
