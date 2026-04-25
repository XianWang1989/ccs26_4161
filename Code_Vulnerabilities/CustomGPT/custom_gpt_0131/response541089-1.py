
import tensorflow as tf
import numpy as np

# Sample data preparation function for CBOW
def create_dataset(words, window_size=2):
    dataset = []
    for i in range(window_size, len(words) - window_size):
        context = words[i-window_size:i] + words[i+1:i+window_size+1]
        target = words[i]
        dataset.append((context, target))
    return dataset

# Example word list
words = ['I', 'love', 'to', 'learn', 'about', 'machine', 'learning']
data = create_dataset(words)

# Preparing input and output
train_inputs, train_labels = [], []
for context, target in data:
    train_inputs.append(context)
    train_labels.append(target)

# Define the CBOW model setup
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=len(vocab), output_dim=embedding_size, input_length=2 * window_size),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(len(vocab), activation='softmax')
])

# Compile and train the model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')
model.fit(np.array(train_inputs), np.array(train_labels), epochs=100)
