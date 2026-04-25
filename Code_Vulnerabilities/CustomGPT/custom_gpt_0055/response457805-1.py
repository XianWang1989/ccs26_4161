
import matplotlib.pyplot as plt

event_index = ['event 1', 'event 2', 'event 3', 'event 4', 'event 5',
               'event 6', 'event 7', 'event 8', 'event 9', 'event 10']
list1 = [0.7, 0.8, 0.8, 0.9, 0.8, 0.7, 0.6, 0.9, 1.0, 0.9]
list2 = [0.2, 0.3, 0.1, 0.0, 0.2, 0.1, 0.3, 0.1, 0.2, 0.1]
list3 = [0.4, 0.6, 0.4, 0.5, 0.4, 0.5, 0.6, 0.4, 0.5, 0.4]
list4 = [78, 87, 77, 65, 89, 98, 74, 94, 85, 73]
list5 = [16, 44, 14, 55, 34, 36, 76, 54, 43, 32]

fig = plt.figure(figsize=(10, 6))  # Create a new figure
ax1 = fig.add_subplot(211)  # First subplot
ax2 = ax1.twinx()  # Twin y-axis for list4

# Plotting in the first subplot
ax1.plot(list1, 'bo-', label='list1')
ax1.plot(list2, 'go-', label='list2')
ax1.plot(list3, 'ro-', label='list3')
ax2.plot(list4, 'yo-', label='list4')

ax1.set_ylim(0, 1)
ax1.set_xlim(0, len(event_index)-1)  # Corrected to fit the index range
ax1.set_ylabel('Some values', fontsize=12)
ax2.set_ylabel('% values', fontsize=12)
ax2.set_ylim(0, 100)

# Second subplot
ax3 = fig.add_subplot(212)
ax3.plot(list4, 'yo-', label='list4')
ax3.plot(list5, 'mo-', label='list5')

ax3.set_xlim(0, len(event_index)-1)  # Corrected x-axis limits
ax3.set_ylabel('% values', fontsize=12)
ax3.set_xticks(range(len(event_index)))  # Set x-ticks to match event indices
ax3.set_xticklabels(event_index)

# Adding legend
lines = [*ax1.lines, *ax2.lines, *ax3.lines]
labels = [l.get_label() for l in lines]
ax3.legend(lines, labels, loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3)  # Centered legend

# Titles
plt.suptitle('Some trends', fontsize=17, y=1.02)  # Separated from plots
subtitle_string = 'Upper panel: list 1, 2, 3, and 4 | Lower panel: list 4 and 5'
plt.figtext(0.5, 0.93, subtitle_string, ha='center', fontsize=10)  # Manual subtitle placement

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.95])  # Allow tight layout with space for title
plt.show()
