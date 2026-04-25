
import matplotlib.pyplot as plt

event_index = ['event 1', 'event 2', 'event 3', 'event 4', 
               'event 5', 'event 6', 'event 7', 'event 8', 'event 9', 'event 10']
list1 = [0.7, 0.8, 0.8, 0.9, 0.8, 0.7, 0.6, 0.9, 1.0, 0.9]
list2 = [0.2, 0.3, 0.1, 0.0, 0.2, 0.1, 0.3, 0.1, 0.2, 0.1]
list3 = [0.4, 0.6, 0.4, 0.5, 0.4, 0.5, 0.6, 0.4, 0.5, 0.4]
list4 = [78, 87, 77, 65, 89, 98, 74, 94, 85, 73]
list5 = [16, 44, 14, 55, 34, 36, 76, 54, 43, 32]

fig, (ax1, ax3) = plt.subplots(2, 1, figsize=(10, 8))  # Create subplots
ax2 = ax1.twinx()  # Create twin y-axis for ax1

# First subplot: list 1, 2, 3, and 4
line1 = ax1.plot(event_index, list1, 'bo-', label='list1')
line2 = ax1.plot(event_index, list2, 'go-', label='list2')
line3 = ax1.plot(event_index, list3, 'ro-', label='list3')
line4 = ax2.plot(event_index, list4, 'yo-', label='list4')

ax1.set_ylim(0, 1)
ax2.set_ylim(0, 100)
ax1.set_ylabel('Some values', fontsize=12)
ax2.set_ylabel('% values', fontsize=12)

# Second subplot: list 4 and 5
ax3.plot(event_index, list4, 'yo-', label='list4')
line5 = ax3.plot(event_index, list5, 'mo-', label='list5')

# Assigning labels for the legend
lines = line1 + line2 + line3 + line4 + line5
labels = [l.get_label() for l in lines]
ax3.legend(lines, labels, loc='lower center', bbox_to_anchor=(0.5, -0.1), ncol=5)

ax3.set_ylabel('% values', fontsize=12)
ax3.set_xlabel('events')
ax3.set_xlim(event_index[0], event_index[-1])  # Set correct x limits

# Remove y-ticks on the second subplot
ax3.yaxis.set_visible(False)

# Titles
plt.suptitle('Some trends', y=1.02, fontsize=17)  # Adjust title position
plt.title('Upper panel: list 1, 2, 3, and 4 | Lower panel: list 4 and 5', fontsize=10)
fig.tight_layout(pad=3.0)  # Adjust layout for better spacing

plt.show()
