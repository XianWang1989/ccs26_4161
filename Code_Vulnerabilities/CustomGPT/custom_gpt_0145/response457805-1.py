
import matplotlib.pyplot as plt

# Initialize data
event_index = ['event 1', 'event 2', 'event 3', 'event 4', 'event 5', 'event 6', 'event 7', 'event 8', 'event 9', 'event 10']
list1 = [0.7, 0.8, 0.8, 0.9, 0.8, 0.7, 0.6, 0.9, 1.0, 0.9]
list2 = [0.2, 0.3, 0.1, 0.0, 0.2, 0.1, 0.3, 0.1, 0.2, 0.1]
list3 = [0.4, 0.6, 0.4, 0.5, 0.4, 0.5, 0.6, 0.4, 0.5, 0.4]
list4 = [78, 87, 77, 65, 89, 98, 74, 94, 85, 73]
list5 = [16, 44, 14, 55, 34, 36, 76, 54, 43, 32]

# Create figure and subplots
fig = plt.figure(figsize=(10, 6))  # Adjust figure size if necessary
ax1 = fig.add_subplot(211)  # First subplot: list 1,2,3, and 4
ax2 = ax1.twinx()  # Twin y-axis
ax3 = fig.add_subplot(212)  # Second subplot: list 4 and 5

# Plotting in the first subplot
line1 = ax1.plot(event_index, list1, 'bo-', label='list1')
line2 = ax1.plot(event_index, list2, 'go-', label='list2')
line3 = ax1.plot(event_index, list3, 'ro-', label='list3')
line4 = ax2.plot(event_index, list4, 'yo-', label='list4')

# Configuring the first subplot
ax1.set_ylim(0, 1)
ax1.set_ylabel('Some values', fontsize=12)
ax2.set_ylabel('% values', fontsize=12)
ax2.set_ylim(0, 100)

# Plotting in the second subplot
ax3.set_ylabel('% values', fontsize=12)
ax3.set_xlabel('events')
ax3.plot(event_index, list4, 'yo-', label='list4')
line5 = ax3.plot(event_index, list5, 'mo-', label='list5')

# Assigning labels and centering legend
lines = line1 + line2 + line3 + line4 + line5
labels = [l.get_label() for l in lines]
ax3.legend(lines, labels, loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=5) 

# Adding titles
title_string = 'Some trends'
subtitle_string = 'Upper panel: list 1, 2, 3, and 4 | Lower panel: list 4 and 5'
plt.suptitle(title_string, y=0.95, fontsize=17)  # Adjust title y to move it away from the subplot
plt.text(0.5, 0.93, subtitle_string, ha='center', fontsize=8, transform=fig.transFigure)

# Remove y-ticks from the second subplot if needed
ax3.yaxis.set_ticks([])

# Improve layout
fig.tight_layout(rect=[0, 0.05, 1, 1])  # Adjust layout to make space for the legend and title
plt.show()
