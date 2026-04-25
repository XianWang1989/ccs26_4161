
import matplotlib.pyplot as plt

event_index = ['event 1','event 2','event 3','event 4','event 5','event 6','event 7','event 8','event 9','event 10']
list1 = [0.7, 0.8, 0.8, 0.9, 0.8, 0.7, 0.6, 0.9, 1.0, 0.9]
list2 = [0.2, 0.3, 0.1, 0.0, 0.2, 0.1, 0.3, 0.1, 0.2, 0.1]
list3 = [0.4, 0.6, 0.4, 0.5, 0.4, 0.5, 0.6, 0.4, 0.5, 0.4]
list4 = [78, 87, 77, 65, 89, 98, 74, 94, 85, 73]
list5 = [16, 44, 14, 55, 34, 36, 76, 54, 43, 32]

fig = plt.figure(figsize=(10, 6))  # Set figure size for better layout
ax1 = fig.add_subplot(211)  # First subplot: list 1,2,3, and 4
ax2 = ax1.twinx()  # Creates a twin y-axis for plotting the values of list 4

# Plotting the lists in the first subplot
ax1.plot(list1, 'bo-', label='list1')
ax1.plot(list2, 'go-', label='list2')
ax1.plot(list3, 'ro-', label='list3')
ax2.plot(list4, 'yo-', label='list4')

ax1.set_ylim(0, 1)
ax1.set_xlim(0, len(event_index) - 1)  # Adjust x limits to match list length
ax1.set_ylabel('Some values', fontsize=12)
ax2.set_ylabel('% values', fontsize=12)
ax2.set_ylim(0, 100)
ax2.set_xlim(0, len(event_index) - 1)  # Event labels align with lists

ax3 = fig.add_subplot(212)  # Second subplot: list 4 and 5
ax3.plot(list4, 'yo-', label='list4')
ax3.plot(list5, 'mo-', label='list5')
ax3.set_xlim(0, len(event_index) - 1)  # Adjust x limits to match list length
ax3.set_ylabel('% values', fontsize=12)
ax3.set_xticks(range(len(event_index)))  # Aligning xticks with events
ax3.set_xticklabels(event_index)  # Add x labels on the second subplot

# Assigning legend
lines = ax1.get_lines() + ax3.get_lines()
labels = [l.get_label() for l in lines]
ax3.legend(lines, labels, loc='center', bbox_to_anchor=(0.5, -0.2), ncol=2)  # Centered below x labels

# Adding titles
plt.suptitle('Some trends', y=1.02, fontsize=17)  # Increase the y position for the title
plt.title('Upper panel: list 1, 2, 3, and 4 | Lower panel: list 4 and 5', fontsize=8)
fig.tight_layout()  # Adjust layout to make space

# Optionally, remove y-axis ticks from second subplot
ax3.yaxis.set_ticks([])

plt.show()
