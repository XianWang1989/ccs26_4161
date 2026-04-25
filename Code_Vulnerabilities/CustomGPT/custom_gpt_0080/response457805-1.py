
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

# Subplot 1 - lists 1, 2, 3 and 4
ax2 = ax1.twinx()  # Create twin y-axis
ax1.plot(list1, 'bo-', label='list1')
ax1.plot(list2, 'go-', label='list2')
ax1.plot(list3, 'ro-', label='list3')
ax2.plot(list4, 'yo-', label='list4')
ax1.set_ylim(0, 1)
ax2.set_ylim(0, 100)
ax1.set_ylabel('Some values', fontsize=12)
ax2.set_ylabel('% values', fontsize=12)

# Subplot 2 - lists 4 and 5
ax3.plot(list4, 'yo-', label='list4')
ax3.plot(list5, 'mo-', label='list5')
ax3.set_ylabel('% values', fontsize=12)
ax3.tick_params(axis='y', which='both', left=False)  # Remove y ticks

# Legends
lines = ax1.lines + ax2.lines + ax3.lines  # All lines from both subplots
labels = [l.get_label() for l in lines]
ax3.legend(lines, labels, loc='bottom center', bbox_to_anchor=(0.5, -0.2), ncol=2)

# Titles
plt.suptitle('Some trends', fontsize=17, y=0.95)
plt.title('Upper panel: list 1, 2, 3, and 4 | Lower panel: list 4 and 5', fontsize=8, y=0.9)

# Set x labels
ax3.set_xlabel('Events')
ax1.set_xticks(range(len(event_index)))
ax1.set_xticklabels(event_index, rotation=45)

# Adjust layout
plt.tight_layout()
plt.subplots_adjust(top=0.85, bottom=0.15)  # Adjust space for titles/legends
plt.show()
