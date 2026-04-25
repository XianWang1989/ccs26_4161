
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
fig, (ax1, ax3) = plt.subplots(nrows=2, figsize=(10, 8), gridspec_kw={'height_ratios': [2, 1]})

# First subplot
ax2 = ax1.twinx()  # Create twin y-axis for list4
ax1.plot(event_index, list1, 'bo-', label='list1')
ax1.plot(event_index, list2, 'go-', label='list2')
ax1.plot(event_index, list3, 'ro-', label='list3')
ax2.plot(event_index, list4, 'yo-', label='list4')

ax1.set_ylim(0, 1)
ax1.set_ylabel('Some values', fontsize=12)
ax2.set_ylabel('% values', fontsize=12)
ax2.set_ylim(0, 100)

# Second subplot
ax3.plot(event_index, list4, 'yo-', label='list4')
ax3.plot(event_index, list5, 'mo-', label='list5')
ax3.set_ylabel('% values', fontsize=12)
ax3.set_xlabel('Events', fontsize=12)

# Legend
lines = ax1.get_lines() + ax3.get_lines()
labels = [line.get_label() for line in lines]
ax3.legend(lines, labels, loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=2)

# Titles
plt.suptitle('Some trends', fontsize=17, y=1.02)
plt.title('Upper panel: list 1, 2, 3, and 4 | Lower panel: list 4 and 5', fontsize=8)

# Adjust layout
plt.tight_layout()
plt.show()
