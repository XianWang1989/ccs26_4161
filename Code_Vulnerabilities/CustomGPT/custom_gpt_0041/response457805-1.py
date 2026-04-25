
import matplotlib.pyplot as plt

# Your data
event_index = ['event 1','event 2','event 3','event 4','event 5','event 6','event 7','event 8','event 9','event 10']
list1 = [0.7, 0.8, 0.8, 0.9, 0.8, 0.7, 0.6, 0.9, 1.0, 0.9]
list2 = [0.2, 0.3, 0.1, 0.0, 0.2, 0.1, 0.3, 0.1, 0.2, 0.1]
list3 = [0.4, 0.6, 0.4, 0.5, 0.4, 0.5, 0.6, 0.4, 0.5, 0.4]
list4 = [78, 87, 77, 65, 89, 98, 74, 94, 85, 73]
list5 = [16, 44, 14, 55, 34, 36, 76, 54, 43, 32]

# Create figure and subplots
fig, (ax1, ax3) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)  # Combine creating and sharing x-axis

# Subplot 1
ax2 = ax1.twinx()  # Create a twin y-axis for the first subplot
ax1.plot(list1, 'bo-', label='list1')
ax1.plot(list2, 'go-', label='list2')
ax1.plot(list3, 'ro-', label='list3')
ax2.plot(list4, 'yo-', label='list4')

# Set limits and labels for subplot 1
ax1.set_ylim(0, 1)
ax2.set_ylim(0, 100)
ax1.set_ylabel('Some values', fontsize=12)
ax2.set_ylabel('% values', fontsize=12)

# Subplot 2
ax3.plot(list4, 'yo-', label='list4')
ax3.plot(list5, 'mo-', label='list5')

# Format legend
lines = ax1.get_lines() + ax3.get_lines()
labels = [line.get_label() for line in lines]
ax3.legend(lines, labels, loc='lower center', bbox_to_anchor=(0.5, -0.2), ncol=5)  # Centered below x-axis

# X-axis and title
ax3.set_xlabel('events')
fig.suptitle('Some trends', y=0.95, fontsize=17)  # Space out the title from subplots
ax3.set_title('Upper panel: list 1, 2, 3, and 4 | Lower panel: list 4 and 5', fontsize=8, loc='center')

# Remove y-axis ticks from second subplot
ax3.yaxis.set_visible(False)

# Layout adjustments
plt.tight_layout(rect=[0, 0, 1, 0.95])  # Adjust layout so that there’s space for the title
plt.xticks(range(len(event_index)), event_index)  # Set x-ticks
plt.show()
