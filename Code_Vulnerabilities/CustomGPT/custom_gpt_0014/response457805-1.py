
import matplotlib.pyplot as plt

# Data
event_index = ['event 1', 'event 2', 'event 3', 'event 4', 'event 5', 
               'event 6', 'event 7', 'event 8', 'event 9', 'event 10']
list1 = [0.7, 0.8, 0.8, 0.9, 0.8, 0.7, 0.6, 0.9, 1.0, 0.9]
list2 = [0.2, 0.3, 0.1, 0.0, 0.2, 0.1, 0.3, 0.1, 0.2, 0.1]
list3 = [0.4, 0.6, 0.4, 0.5, 0.4, 0.5, 0.6, 0.4, 0.5, 0.4]
list4 = [78, 87, 77, 65, 89, 98, 74, 94, 85, 73]
list5 = [16, 44, 14, 55, 34, 36, 76, 54, 43, 32]

# Create figure and axes
fig, (ax1, ax3) = plt.subplots(nrows=2, sharex=True, figsize=(10, 8))
ax2 = ax1.twinx()  # Twin y-axis for ax1

# First subplot with four lists
ax1.plot(list1, 'bo-', label='list1')
ax1.plot(list2, 'go-', label='list2')
ax1.plot(list3, 'ro-', label='list3')
ax2.plot(list4, 'yo-', label='list4')

ax1.set_ylim(0, 1)
ax1.set_ylabel('Some values', fontsize=12)
ax2.set_ylabel('% values', fontsize=12)
ax2.set_ylim(0, 100)

# Second subplot with two lists
ax3.plot(list4, 'yo-', label='list4')
ax3.plot(list5, 'mo-', label='list5')

ax3.set_ylabel('% values', fontsize=12)
ax3.set_ylim(0, 100)
ax3.tick_params(axis='y', which='both', left=False)  # Remove y-axis ticks

# Assigning labels
lines = ax1.get_lines() + ax3.get_lines()
labels = [line.get_label() for line in lines]

# Add legend
ax3.legend(lines, labels, loc='center', ncol=5, bbox_to_anchor=(0.5, -0.2))

# Titles and subtitles
title_string = 'Some trends'
subtitle_string = 'Upper panel: list 1, 2, 3, and 4 | Lower panel: list 4 and 5'
fig.suptitle(title_string, y=0.97, fontsize=17)
plt.figtext(0.5, 0.92, subtitle_string, ha='center', fontsize=9)

# Adjust layout
fig.tight_layout(rect=[0, 0.03, 1, 1])  # Make space for the title
plt.xticks(ticks=range(len(event_index)), labels=event_index)  # Set x-ticks

plt.show()
