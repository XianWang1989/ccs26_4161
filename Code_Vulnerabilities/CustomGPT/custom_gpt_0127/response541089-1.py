
import tensorflow as tf
import numpy as np
from sklearn.preprocessing import OneHotEncoder

# Example data
sentences = [["the", "cat", "sat", "on", "the", "mat"]]
window_size = 2  # Number of context words on each side

# Build vocabulary
vocab = list(set(word for sentence in sentences for word in sentence))
word_to_id = {word: i for i, word in enumerate(vocab)}
id_to_word = {i: word for i, word in enumerate(vocab)}

# Prepare training data for CBOW
train_inputs = []
train_labels = []

for sentence in sentences:
    for i, target_word in enumerate(sentence):
        context_words = []
        for j in range(-window_size, window_size + 1):
            if j != 0 and (0 <= i + j < len(sentence)):
                context_words.append(word_to_id[sentence[i + j]])
        if len(context_words) == 2 * window_size:
            train_inputs.append(context_words)
            train_labels.append(word_to_id[target_word])

# One-hot encoding labels
encoder = OneHotEncoder(sparse=False)
train_labels = encoder.fit_transform(np.array(train_labels).reshape(-1, 1))

# Define model
embedding_dim = 10
vocab_size = len(vocab)

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=2 * window_size),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(vocab_size, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train model
model.fit(np.array(train_inputs), np.array(train_labels), epochs=100)

# Example input for prediction
context_example = np.array([[word_to_id["the"], word_to_id["cat"], word_to_id["on"], word_to_id["the"]]])
predicted_word = model.predict(context_example)
predicted_word_id = np.argmax(predicted_word)
print("Predicted word:", id_to_word[predicted_word_id])
