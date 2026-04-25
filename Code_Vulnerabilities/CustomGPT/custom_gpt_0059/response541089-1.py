
import numpy as np
import tensorflow as tf

# Sample data
# Let's assume we have a context of size 2
context_words = [['word1', 'word2'], 'word3']  # context: word1, word2 -> target: word3
# Create a vocabulary
vocab = {'word1': 0, 'word2': 1, 'word3': 2}
vocab_size = len(vocab)

# Prepare training data
train_inputs = np.array([[vocab[w] for w in context_words[0]]])
train_labels = np.array([[vocab[context_words[1]]]])

# Hyperparameters
embedding_dim = 128
batch_size = 1
num_epochs = 1000

# Model creation
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=2),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(vocab_size, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

# Train the model
model.fit(train_inputs, train_labels, epochs=num_epochs)

# Example prediction
sample_context = np.array([[0, 1]])  # word1 and word2 as input
predicted_word = model.predict(sample_context)
predicted_index = np.argmax(predicted_word)
predicted_word = list(vocab.keys())[list(vocab.values()).index(predicted_index)]

print("Predicted word:", predicted_word)
