
import matplotlib.pyplot as plt

event_index = ['event 1', 'event 2', 'event 3', 'event 4', 'event 5', 
               'event 6', 'event 7', 'event 8', 'event 9', 'event 10']
list1 = [0.7, 0.8, 0.8, 0.9, 0.8, 0.7, 0.6, 0.9, 1.0, 0.9]
list2 = [0.2, 0.3, 0.1, 0.0, 0.2, 0.1, 0.3, 0.1, 0.2, 0.1]
list3 = [0.4, 0.6, 0.4, 0.5, 0.4, 0.5, 0.6, 0.4, 0.5, 0.4]
list4 = [78, 87, 77, 65, 89, 98, 74, 94, 85, 73]
list5 = [16, 44, 14, 55, 34, 36, 76, 54, 43, 32]

fig = plt.figure(figsize=(10, 8))  # Increased size for better visibility
ax1 = fig.add_subplot(211)  # First subplot
ax2 = ax1.twinx()  # Twin y-axis for list4

# Plotting data
ax1.plot(list1, 'bo-', label='list1')
ax1.plot(list2, 'go-', label='list2')
ax1.plot(list3, 'ro-', label='list3')
ax2.plot(list4, 'yo-', label='list4')

# Setting limits and labels
ax1.set_ylim(0, 1)
ax1.set_xlim(0, len(event_index) - 1)  # Adjusted to plot all points
ax1.set_ylabel('Some values', fontsize=12)
ax2.set_ylabel('% values', fontsize=12)
ax2.set_ylim(0, 100)

# Second subplot
ax3 = fig.add_subplot(212)
ax3.set_xlim(0, len(event_index) - 1)
ax3.set_ylabel('% values', fontsize=12)

# Plotting list4 and list5
ax3.plot(list4, 'yo-', label='list4')
ax3.plot(list5, 'mo-', label='list5')

# Assigning legend
lines = ax1.get_lines() + ax3.get_lines()  # Combine lines from both subplots
labels = [l.get_label() for l in lines]
ax3.legend(lines, labels, loc='lower center', bbox_to_anchor=(0.5, -0.1), ncol=5)

# Setting titles
plt.suptitle('Some trends', y=0.95, fontsize=17)
plt.title('Upper panel: list 1, 2, 3, and 4 | Lower panel: list 4 and 5', fontsize=10, loc='center')

# Remove y-axis ticks from ax3
ax3.tick_params(axis='y', which='both', left=False)

# Adjust layout
fig.tight_layout(rect=[0.05, 0.05, 0.95, 0.95])  # Add padding for title area
plt.show()
