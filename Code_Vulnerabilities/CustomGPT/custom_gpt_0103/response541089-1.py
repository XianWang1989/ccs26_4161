
import tensorflow as tf
import numpy as np

# Sample data
# Let's say we have a vocabulary of 5 words
vocabulary_size = 5
window_size = 2  # Context window size

# Dummy data: target word and context words
words = [0, 1, 2, 3, 4]
train_inputs = []
train_labels = []

# Create training data for CBOW
for i in range(window_size, len(words) - window_size):
    context = words[i-window_size:i] + words[i+1:i+window_size+1]
    target = words[i]
    train_inputs.append(context)
    train_labels.append(target)

train_inputs = np.array(train_inputs)
train_labels = np.array(train_labels)

# One-hot encoding for labels
train_labels = tf.keras.utils.to_categorical(train_labels, num_classes=vocabulary_size)

# CBOW model using Keras
model = tf.keras.Sequential()
model.add(tf.keras.layers.Embedding(vocabulary_size, 10, input_length=2*window_size))
model.add(tf.keras.layers.GlobalAveragePooling1D())
model.add(tf.keras.layers.Dense(vocabulary_size, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(train_inputs, train_labels, epochs=100)

# Now you can use model.predict() for new inputs
