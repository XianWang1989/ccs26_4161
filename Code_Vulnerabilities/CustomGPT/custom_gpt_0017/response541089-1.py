
import tensorflow as tf
import numpy as np

# Sample data
# Example: "the cat sat on the mat"
data = 'the cat sat on the mat'
words = data.split()
vocab = set(words)
word_to_index = {word: index for index, word in enumerate(vocab)}
index_to_word = {index: word for index, word in enumerate(vocab)}

# Hyperparameters
embedding_size = 2  # Dimension of embedding vector
window_size = 2  # Context window size

# Preparing the dataset
train_inputs = []
train_labels = []

for i in range(window_size, len(words) - window_size):
    context = []
    for j in range(-window_size, window_size + 1):
        if j != 0:
            context.append(word_to_index[words[i + j]])
    train_inputs.append(context)  # context words as input
    train_labels.append(word_to_index[words[i]])  # target word as output

# Convert to NumPy arrays
train_inputs = np.array(train_inputs)
train_labels = np.array(train_labels)

# Build the model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=len(vocab), output_dim=embedding_size, input_length=2 * window_size),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(len(vocab), activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

# Train the model
model.fit(train_inputs, train_labels, epochs=100)

# Example of usage
print(model.predict(np.array([[word_to_index['the'], word_to_index['cat'], word_to_index['mat'], word_to_index['sat']]])))
