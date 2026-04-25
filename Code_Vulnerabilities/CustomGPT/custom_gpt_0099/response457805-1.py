
import matplotlib.pyplot as plt

# Data
event_index = ['event 1','event 2','event 3','event 4','event 5','event 6','event 7','event 8','event 9','event 10']
list1 = [0.7, 0.8, 0.8, 0.9, 0.8, 0.7, 0.6, 0.9, 1.0, 0.9]
list2 = [0.2, 0.3, 0.1, 0.0, 0.2, 0.1, 0.3, 0.1, 0.2, 0.1]
list3 = [0.4, 0.6, 0.4, 0.5, 0.4, 0.5, 0.6, 0.4, 0.5, 0.4]
list4 = [78, 87, 77, 65, 89, 98, 74, 94, 85, 73]
list5 = [16, 44, 14, 55, 34, 36, 76, 54, 43, 32]

# Create figure and subplots
fig, (ax1, ax3) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Plot first subplot
ax2 = ax1.twinx()  # create twin y-axis
ax1.plot(event_index, list1, 'bo-', label='list1')
ax1.plot(event_index, list2, 'go-', label='list2')
ax1.plot(event_index, list3, 'ro-', label='list3')
ax2.plot(event_index, list4, 'yo-', label='list4')

# Set limits and labels
ax1.set_ylim(0, 1)
ax2.set_ylim(0, 100)
ax1.set_ylabel('Some values', fontsize=12)
ax2.set_ylabel('% values', fontsize=12)

# Plot second subplot
ax3.plot(event_index, list4, 'yo-', label='list4')
ax3.plot(event_index, list5, 'mo-', label='list5')
ax3.set_ylabel('% values', fontsize=12)
ax3.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2)  # Centered legend below subplot

# Set x-axis label and titles
ax3.set_xlabel('Events', fontsize=12)
plt.suptitle('Some Trends', y=0.95, fontsize=17)  # Adjust title position
plt.title('Upper panel: list 1, 2, 3, and 4 | Lower panel: list 4 and 5', fontsize=8)

# Remove y-axis ticks from the second subplot
ax3.yaxis.set_ticks([])

# Adjust layout to prevent overlap
plt.tight_layout(rect=[0, 0, 1, 0.95])  # Leave room for the super title

# Show plot
plt.show()
