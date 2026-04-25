
import matplotlib.pyplot as plt

# Data lists
event_index = ['event 1', 'event 2', 'event 3', 'event 4', 'event 5', 
               'event 6', 'event 7', 'event 8', 'event 9', 'event 10']
list1 = [0.7, 0.8, 0.8, 0.9, 0.8, 0.7, 0.6, 0.9, 1.0, 0.9]
list2 = [0.2, 0.3, 0.1, 0.0, 0.2, 0.1, 0.3, 0.1, 0.2, 0.1]
list3 = [0.4, 0.6, 0.4, 0.5, 0.4, 0.5, 0.6, 0.4, 0.5, 0.4]
list4 = [78, 87, 77, 65, 89, 98, 74, 94, 85, 73]
list5 = [16, 44, 14, 55, 34, 36, 76, 54, 43, 32]

# Create figure and subplots
fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(211)  # First subplot
ax2 = ax1.twinx()           # Twin y-axis for subplot 1

# Plotting in the first subplot
line1 = ax1.plot(list1, 'bo-', label='list1')
line2 = ax1.plot(list2, 'go-', label='list2')
line3 = ax1.plot(list3, 'ro-', label='list3')
line4 = ax2.plot(list4, 'yo-', label='list4')

# Setting limits and labels for subplot 1
ax1.set_ylim(0, 1)
ax1.set_xlim(0, len(event_index) - 1)
ax1.set_ylabel('Some values', fontsize=12)
ax2.set_ylabel('% values', fontsize=12)
ax2.set_ylim(0, 100)

# Second subplot
ax3 = fig.add_subplot(212)
ax3.set_xlim(0, len(event_index) - 1)
ax3.set_ylabel('% values', fontsize=12)
ax3.plot(list4, 'yo-', label='list4')
line5 = ax3.plot(list5, 'mo-', label='list5')

# Legend
lines = line1 + line2 + line3 + line4 + line5
labels = [l.get_label() for l in lines]
ax3.legend(lines, labels, loc='center', bbox_to_anchor=(0.5, -0.15), ncol=5)

# Titles
plt.title('Some trends', fontsize=17, pad=20)
subtitle_string = 'Upper panel: list 1, 2, 3, and 4 | Lower panel: list 4 and 5'
plt.suptitle(subtitle_string, fontsize=8, y=0.93)

# Remove y-axis ticks in the second subplot
ax3.yaxis.set_ticks([])

# Layout adjustment
fig.tight_layout()
plt.subplots_adjust(top=0.85)  # Adjust for title space

# Set the x-ticks to show event labels
ax1.set_xticks(range(len(event_index)))
ax1.set_xticklabels(event_index, rotation=45)
ax3.set_xticks(range(len(event_index)))
ax3.set_xticklabels(event_index, rotation=45)

plt.show()
