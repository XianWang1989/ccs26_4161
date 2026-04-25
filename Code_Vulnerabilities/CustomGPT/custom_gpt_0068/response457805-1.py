
import matplotlib.pyplot as plt

event_index = ['event 1', 'event 2', 'event 3', 'event 4', 'event 5', 'event 6', 'event 7', 'event 8', 'event 9', 'event 10']
list1 = [0.7, 0.8, 0.8, 0.9, 0.8, 0.7, 0.6, 0.9, 1.0, 0.9]
list2 = [0.2, 0.3, 0.1, 0.0, 0.2, 0.1, 0.3, 0.1, 0.2, 0.1]
list3 = [0.4, 0.6, 0.4, 0.5, 0.4, 0.5, 0.6, 0.4, 0.5, 0.4]
list4 = [78, 87, 77, 65, 89, 98, 74, 94, 85, 73]
list5 = [16, 44, 14, 55, 34, 36, 76, 54, 43, 32]

fig, (ax1, ax3) = plt.subplots(2, 1, sharex=True, figsize=(10, 8))  # Create subplots
ax2 = ax1.twinx()  # Create a twin y-axis for plotting the values of list 4

# First subplot: list 1, 2, 3, and 4
line1 = ax1.plot(list1, 'bo-', label='list1')
line2 = ax1.plot(list2, 'go-', label='list2')
line3 = ax1.plot(list3, 'ro-', label='list3')
line4 = ax2.plot(list4, 'yo-', label='list4')

ax1.set_ylim(0, 1)
ax1.set_ylabel('Some values', fontsize=12)
ax2.set_ylabel('% values', fontsize=12)
ax2.set_ylim(0, 100)
ax1.legend(loc='upper left')  # Place legend in the upper left of the first subplot

# Second subplot: list 4 and 5
ax3.plot(list4, 'yo-', label='list4')
line5 = ax3.plot(list5, 'mo-', label='list5')
ax3.set_ylabel('% values', fontsize=12)
ax3.set_xlabel('Events', fontsize=12)

# Assigning labels and configuring legend
lines = line4 + line5
labels = [l.get_label() for l in lines]
ax3.legend(lines, labels, loc='lower center', bbox_to_anchor=(0.5, -0.1), ncol=2)  # Centered legend below x-axis

# Adding titles
plt.suptitle('Some trends', y=0.95, fontsize=17)  # Adjust y to position the title higher
plt.title('Upper panel: list 1, 2, 3, and 4 | Lower panel: list 4 and 5', fontsize=10)

# Remove y-axis ticks for the second subplot
ax3.yaxis.set_ticks([])

# Adjust layout to prevent overlaps
plt.tight_layout()
plt.subplots_adjust(top=0.93, bottom=0.1)  # Adjust top for the subtitle and bottom for the x labels

plt.show()
