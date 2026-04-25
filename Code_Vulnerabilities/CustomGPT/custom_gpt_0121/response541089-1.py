
import numpy as np
import tensorflow as tf

# Sample data: a simple sentence
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
vocab = set(words)
word2int = {word: i for i, word in enumerate(vocab)}
int2word = {i: word for i, word in enumerate(vocab)}

# Hyperparameters
window_size = 2
embedding_size = 10

# Generate training data for CBOW
train_inputs, train_labels = [], []
for i in range(window_size, len(words) - window_size):
    context = [word2int[words[i + j]] for j in range(-window_size, window_size + 1) if j != 0]
    target = word2int[words[i]]
    train_inputs.append(context)
    train_labels.append(target)

# Convert to numpy arrays
train_inputs = np.array(train_inputs)
train_labels = np.array(train_labels)

# Build the CBOW model
# Input layer
inputs = tf.keras.layers.Input(shape=(train_inputs.shape[1],))
# Embedding layer
embeddings = tf.keras.layers.Embedding(input_dim=len(vocab), output_dim=embedding_size)(inputs)
# Average the context embeddings
context = tf.keras.layers.Lambda(lambda x: tf.reduce_mean(x, axis=1))(embeddings)
# Output layer
outputs = tf.keras.layers.Dense(len(vocab), activation='softmax')(context)

model = tf.keras.Model(inputs=inputs, outputs=outputs)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_inputs, train_labels, epochs=100)

# Here train_inputs contains context words and train_labels contains target words
