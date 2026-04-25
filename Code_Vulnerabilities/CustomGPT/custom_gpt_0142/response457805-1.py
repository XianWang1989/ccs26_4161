
import matplotlib.pyplot as plt

event_index=['event 1','event 2','event 3','event 4','event 5','event 6','event 7','event 8','event 9','event 10']
list1 = [0.7,0.8,0.8,0.9,0.8,0.7,0.6,0.9,1.0,0.9]
list2 = [0.2,0.3,0.1,0.0,0.2,0.1,0.3,0.1,0.2,0.1]
list3 = [0.4,0.6,0.4,0.5,0.4,0.5,0.6,0.4,0.5,0.4]
list4 = [78,87,77,65,89,98,74,94,85,73]
list5 = [16,44,14,55,34,36,76,54,43,32]

fig = plt.figure()
ax1 = fig.add_subplot(211)  # First subplot
ax2 = ax1.twinx()  # Twin y-axis
# Plot the data
ax1.plot(list1, 'bo-', label='list1')
ax1.plot(list2, 'go-', label='list2')
ax1.plot(list3, 'ro-', label='list3')
ax2.plot(list4, 'yo-', label='list4')

# Set limits and labels
ax1.set_ylim(0, 1)
ax2.set_ylim(0, 100)
ax1.set_ylabel('Some values', fontsize=12)
ax2.set_ylabel('% values', fontsize=12)

# Second subplot
ax3 = fig.add_subplot(212)
ax3.plot(list4, 'yo-', label='list4')
ax3.plot(list5, 'mo-', label='list5')

# Set limits and labels for second subplot
ax3.set_ylabel('% values', fontsize=12)
ax3.set_xlabel('events')
ax3.set_xticks(range(len(event_index)))  # Set x-ticks to the length of events
ax3.set_xticklabels(event_index, rotation=45)
ax3.legend(bbox_to_anchor=(0.5, -0.15), loc='upper center', ncol=2)  # Centered legend below

# Titles and subtitles
plt.suptitle('Some trends', fontsize=17, y=1.05)  # Increase y-value to move title down
plt.title('Upper panel: list 1, 2, 3, and 4 | Lower panel: list 4 and 5', fontsize=8, y=0.98)

# Adjust layout
fig.tight_layout(rect=[0, 0.03, 1, 0.95])  # Manage the layout with rect space for title

plt.show()
