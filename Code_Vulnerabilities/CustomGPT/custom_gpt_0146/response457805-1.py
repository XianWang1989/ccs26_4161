
import matplotlib.pyplot as plt

# Your data
event_index = ['event 1','event 2','event 3','event 4','event 5','event 6','event 7','event 8','event 9','event 10']
list1 = [0.7,0.8,0.8,0.9,0.8,0.7,0.6,0.9,1.0,0.9]
list2 = [0.2,0.3,0.1,0.0,0.2,0.1,0.3,0.1,0.2,0.1]
list3 = [0.4,0.6,0.4,0.5,0.4,0.5,0.6,0.4,0.5,0.4]
list4 = [78,87,77,65,89,98,74,94,85,73]
list5 = [16,44,14,55,34,36,76,54,43,32]

# Create figure and axes
fig = plt.figure(figsize=(10, 8))  # Increased figure size for better layout
ax1 = fig.add_subplot(211)  # First subplot
ax2 = ax1.twinx()  # Twin y-axis for plotting the values of list 4
ax3 = fig.add_subplot(212)  # Second subplot

# Plotting on the first subplot
line1 = ax1.plot(list1, 'bo-', label='list1')
line2 = ax1.plot(list2, 'go-', label='list2')
line3 = ax1.plot(list3, 'ro-', label='list3')
line4 = ax2.plot(list4, 'yo-', label='list4')

# Setting x and y limits for ax1
ax1.set_ylim(0, 1)
ax1.set_xlim(0, len(event_index) - 1)  # Corrected to match indices
ax1.set_ylabel('Some values', fontsize=12)

# Configure the twin y-axis
ax2.set_ylabel('% values', fontsize=12)
ax2.set_ylim(0, 100)

# Plotting on the second subplot
ax3.set_xlim(0, len(event_index) - 1)  # Set limits to match the data
ax3.set_ylabel('% values', fontsize=12)

# Plotting list4 and list5 on second subplot
line5 = ax3.plot(list4, 'yo-', label='list4')
line6 = ax3.plot(list5, 'mo-', label='list5')

# Assigning labels for legend
lines = line1 + line2 + line3 + line4 + line5 + line6
labels = [l.get_label() for l in lines]

# Legend positioning and adjustment
ax3.legend(lines, labels, loc='lower center', bbox_to_anchor=(0.5, -0.2), ncol=5, fontsize=10, frameon=False)  # Centered below x-labels

# Set x-ticks for both subplots
ax1.set_xticks(range(len(event_index)))
ax1.set_xticklabels(event_index, rotation=45)
ax3.set_xticks(range(len(event_index)))
ax3.set_xticklabels(event_index, rotation=45)

# Improve spacing and title configurations
plt.suptitle('Some trends', fontsize=17, y=0.97)  # moved up slightly
plt.title('Upper panel: list 1, 2, 3, and 4 | Lower panel: list 4 and 5', fontsize=8, y=0.93)  # moved up slightly

# Remove y-axis ticks from second subplot
ax3.get_yaxis().set_visible(False)

# Adjust layout
fig.tight_layout()
plt.subplots_adjust(top=0.85, bottom=0.2)  # Adjust layout for suptitle and legend
plt.show()
