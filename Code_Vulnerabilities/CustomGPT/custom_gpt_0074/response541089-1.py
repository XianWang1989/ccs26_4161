
import numpy as np
import tensorflow as tf

# Sample data
words = ['I', 'love', 'machine', 'learning']
word_to_index = {word: i for i, word in enumerate(words)}
index_to_word = {i: word for i, word in enumerate(words)}

# Parameters
window_size = 2
num_words = len(words)
embedding_size = 4  # Size of embedding vector

# Generate training data for CBOW
train_pairs = []
for i in range(window_size, len(words) - window_size):
    context = [word_to_index[words[i - j]] for j in range(window_size, 0, -1)] + \
              [word_to_index[words[i + j]] for j in range(1, window_size + 1)]
    target = word_to_index[words[i]]
    train_pairs.append((context, target))

# Prepare the training data
train_inputs = np.array([item[0] for item in train_pairs])
train_labels = np.array([item[1] for item in train_pairs])

# Create the CBOW model
inputs = tf.keras.Input(shape=(window_size * 2,))
embeddings = tf.keras.layers.Embedding(num_words, embedding_size)(inputs)
context_vector = tf.keras.layers.Lambda(lambda x: tf.reduce_mean(x, axis=1))(embeddings)
outputs = tf.keras.layers.Dense(num_words, activation='softmax')(context_vector)

model = tf.keras.Model(inputs=inputs, outputs=outputs)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')
model.summary()

# Training the model
model.fit(train_inputs, train_labels, epochs=100)
