
import tensorflow as tf
import numpy as np

# Sample data
sentences = [["the", "cat", "sat", "on", "the", "mat"]]
words = list(set([word for sentence in sentences for word in sentence]))
word_to_index = {word: idx for idx, word in enumerate(words)}

# Parameters
embedding_size = 50  # Size of the embedding vector
window_size = 2  # Window size
vocab_size = len(words)

# Prepare training data
train_inputs = []
train_labels = []

for sentence in sentences:
    for i, word in enumerate(sentence):
        context_words = []
        for j in range(-window_size, window_size + 1):
            if j != 0 and 0 <= i + j < len(sentence):
                context_words.append(word_to_index[sentence[i + j]])
        train_inputs.append(context_words)
        train_labels.append(word_to_index[word])

# Convert to array
train_inputs = np.array(train_inputs)
train_labels = np.array(train_labels)

# CBOW model
model = tf.keras.Sequential()
model.add(tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=embedding_size, input_length=window_size * 2))
model.add(tf.keras.layers.Lambda(lambda x: tf.reduce_mean(x, axis=1)))  # Average the embeddings
model.add(tf.keras.layers.Dense(vocab_size, activation='softmax'))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

# Train the model
model.fit(train_inputs, train_labels, epochs=100)

# Example prediction
predictions = model.predict(train_inputs)
print(predictions)
