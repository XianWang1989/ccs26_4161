
import numpy as np
import tensorflow as tf

# Sample data: sentences represented as lists of word indices
# For simplicity, let's say we have a vocabulary size of 5
sentences = [
    [0, 1, 2, 3, 4],
    [2, 1, 3, 4, 0],
    # more sentences
]

# Parameters
vocab_size = 5
embedding_dim = 16
window_size = 2

# Prepare data for CBOW
train_inputs = []
train_labels = []

for sentence in sentences:
    for i in range(window_size, len(sentence) - window_size):
        context = []
        for j in range(i - window_size, i + window_size + 1):
            if j != i:
                context.append(sentence[j])
        train_inputs.append(context)
        train_labels.append(sentence[i])

# Convert to numpy arrays
train_inputs = np.array(train_inputs)
train_labels = np.array(train_labels)

# Create the CBOW model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=window_size * 2),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(vocab_size, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_inputs, train_labels, epochs=100)
