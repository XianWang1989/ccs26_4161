
import matplotlib.pyplot as plt

# Data
event_index = ['event 1', 'event 2', 'event 3', 'event 4', 'event 5', 
               'event 6', 'event 7', 'event 8', 'event 9', 'event 10']
list1 = [0.7, 0.8, 0.8, 0.9, 0.8, 0.7, 0.6, 0.9, 1.0, 0.9]
list2 = [0.2, 0.3, 0.1, 0.0, 0.2, 0.1, 0.3, 0.1, 0.2, 0.1]
list3 = [0.4, 0.6, 0.4, 0.5, 0.4, 0.5, 0.6, 0.4, 0.5, 0.4]
list4 = [78, 87, 77, 65, 89, 98, 74, 94, 85, 73]
list5 = [16, 44, 14, 55, 34, 36, 76, 54, 43, 32]

# Create figure and subplots
fig, (ax1, ax3) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# First subplot
ax2 = ax1.twinx()
line1, = ax1.plot(list1, 'bo-', label='list1')
line2, = ax1.plot(list2, 'go-', label='list2')
line3, = ax1.plot(list3, 'ro-', label='list3')
line4, = ax2.plot(list4, 'yo-', label='list4')

ax1.set_ylim(0, 1)
ax2.set_ylim(0, 100)
ax1.set_ylabel('Some values', fontsize=12)
ax2.set_ylabel('% values', fontsize=12)

# Second subplot
ax3.plot(list4, 'yo-', label='list4')
line5, = ax3.plot(list5, 'mo-', label='list5')
ax3.set_ylabel('% values', fontsize=12)
ax3.legend(loc='center', bbox_to_anchor=(0.5, -0.2), ncol=2)

# Setting x-ticks and labels
ax3.set_xticks(range(len(event_index)))
ax3.set_xticklabels(event_index, rotation=45)

# Titles
plt.suptitle('Some trends', fontsize=17, y=0.93)
plt.title('Upper panel: list 1, 2, 3, and 4 | Lower panel: list 4 and 5', fontsize=10)

# Remove y-ticks from the second subplot
ax3.yaxis.set_ticks([])

# Adjust layout
plt.tight_layout(rect=[0, 0.05, 1, 0.95])
plt.show()
