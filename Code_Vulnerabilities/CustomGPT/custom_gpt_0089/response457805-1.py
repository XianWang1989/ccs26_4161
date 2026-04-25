
import matplotlib.pyplot as plt

event_index = ['event 1', 'event 2', 'event 3', 'event 4', 'event 5', 
               'event 6', 'event 7', 'event 8', 'event 9', 'event 10']
list1 = [0.7, 0.8, 0.8, 0.9, 0.8, 0.7, 0.6, 0.9, 1.0, 0.9]
list2 = [0.2, 0.3, 0.1, 0.0, 0.2, 0.1, 0.3, 0.1, 0.2, 0.1]
list3 = [0.4, 0.6, 0.4, 0.5, 0.4, 0.5, 0.6, 0.4, 0.5, 0.4]
list4 = [78, 87, 77, 65, 89, 98, 74, 94, 85, 73]
list5 = [16, 44, 14, 55, 34, 36, 76, 54, 43, 32]

fig = plt.figure(figsize=(10, 8))  # Size of figure
ax1 = fig.add_subplot(211)  # First subplot
ax2 = ax1.twinx()  # Twin y-axis for list4
ax3 = fig.add_subplot(212)  # Second subplot

# Plotting list1, list2, list3 with their labels
line1 = ax1.plot(list1, 'bo-', label='list1')
line2 = ax1.plot(list2, 'go-', label='list2')
line3 = ax1.plot(list3, 'ro-', label='list3')
line4 = ax2.plot(list4, 'yo-', label='list4')

ax1.set_ylim(0, 1)
ax1.set_xlim(0, len(event_index) - 1)  # Adjusted for indexing
ax1.set_ylabel('Some values', fontsize=12)
ax2.set_ylabel('% values', fontsize=12)
ax2.set_ylim(0, 100)

# Plotting for the second subplot
ax3.set_xlim(0, len(event_index) - 1)  # Adjusted for indexing
ax3.plot(list4, 'yo-', label='list4')
line5 = ax3.plot(list5, 'mo-', label='list5')

# Assigning labels and centralizing legend beneath the second subplot
lines = line1 + line2 + line3 + line4 + line5
labels = [l.get_label() for l in lines]
ax3.legend(lines, labels, loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=5)

# Setting titles
plt.suptitle('Some trends', y=0.95, fontsize=17)  # Adjusted position
plt.title('Upper panel: list 1, 2, 3, and 4 | Lower panel: list 4 and 5', fontsize=8)

# Removing y-axis ticks in the second subplot
ax3.yaxis.set_ticks([])

# Improving layout
fig.tight_layout(rect=[0, 0, 1, 0.95])  # Adjust layout to fit titles
plt.xticks(ticks=range(len(event_index)), labels=event_index)  # Set x-tick labels
plt.show()
