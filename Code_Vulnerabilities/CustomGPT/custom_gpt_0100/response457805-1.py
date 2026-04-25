
import matplotlib.pyplot as plt

event_index = ['event 1', 'event 2', 'event 3', 'event 4', 'event 5', 
               'event 6', 'event 7', 'event 8', 'event 9', 'event 10']
list1 = [0.7, 0.8, 0.8, 0.9, 0.8, 0.7, 0.6, 0.9, 1.0, 0.9]
list2 = [0.2, 0.3, 0.1, 0.0, 0.2, 0.1, 0.3, 0.1, 0.2, 0.1]
list3 = [0.4, 0.6, 0.4, 0.5, 0.4, 0.5, 0.6, 0.4, 0.5, 0.4]
list4 = [78, 87, 77, 65, 89, 98, 74, 94, 85, 73]
list5 = [16, 44, 14, 55, 34, 36, 76, 54, 43, 32]

fig = plt.figure(figsize=(10, 6))  # Increased figure size for better layout
ax1 = fig.add_subplot(211)  # First subplot: list 1, 2, 3, and 4
ax2 = ax1.twinx()           # Creates a twin y-axis for plotting the values of list 4

# Plotting lines in subplot 1
line1, = ax1.plot(list1, 'bo-', label='list1')
line2, = ax1.plot(list2, 'go-', label='list2')
line3, = ax1.plot(list3, 'ro-', label='list3')
line4, = ax2.plot(list4, 'yo-', label='list4')

# Configure axes
ax1.set_ylim(0, 1)
ax1.set_xlim(1, len(event_index))
ax1.set_ylabel('Some values', fontsize=12)
ax2.set_ylabel('% values', fontsize=12)
ax2.set_ylim(0, 100)

# Second subplot: list 4 and 5
ax3 = fig.add_subplot(212)
ax3.set_xlim(1, len(event_index))
ax3.set_ylabel('% values', fontsize=12)

# Plotting in subplot 2
ax3.plot(list4, 'yo-', label='list4')
line5, = ax3.plot(list5, 'mo-', label='list5')

# Centering the legend below subplot 2
lines = [line4, line5]
labels = [l.get_label() for l in lines]
ax3.legend(lines, labels, loc='lower center', bbox_to_anchor=(0.5, -0.25), ncol=2)

# Assigning titles
title_string = 'Some trends'
subtitle_string = 'Upper panel: list 1, 2, 3, and 4 | Lower panel: list 4 and 5'

plt.suptitle(title_string, y=0.95, fontsize=17)  # Adjust title y position
plt.title(subtitle_string, fontsize=8, pad=10)  # Added padding for subtitle

# Remove y-axis ticks from the second subplot
ax3.yaxis.set_ticks([])

fig.tight_layout(rect=[0, 0, 1, 0.95])  # Adjusts layout to make space for suptitle
plt.xticks(range(1, len(event_index) + 1), event_index)  # Set x-ticks to use event_index
plt.show()
