
import tensorflow as tf
import numpy as np

# Sample data
words = ["I", "love", "machine", "learning"]
word_to_id = {word: i for i, word in enumerate(words)}
id_to_word = {i: word for word, i in word_to_id.items()}

# Function to generate training data for CBOW
def generate_cbow_data(corpus, window_size=1):
    train_inputs = []
    train_labels = []

    for i in range(window_size, len(corpus) - window_size):
        context = []
        for j in range(i - window_size, i + window_size + 1):
            if j != i:
                context.append(word_to_id[corpus[j]])
        train_inputs.append(context)
        train_labels.append(word_to_id[corpus[i]])

    return np.array(train_inputs), np.array(train_labels)

# Generate training data
train_inputs, train_labels = generate_cbow_data(words)

# TensorFlow model
vocab_size = len(words)
embedding_dim = 2

# Create model
inputs = tf.keras.Input(shape=(2 * 1,))  # Adjusted for window size
embedding = tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=embedding_dim)(inputs)
output = tf.keras.layers.Dense(vocab_size, activation='softmax')(tf.reduce_mean(embedding, axis=1))

model = tf.keras.Model(inputs, output)
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(train_inputs, train_labels, epochs=100)

# Example prediction
input_context = np.array([[word_to_id["I"], word_to_id["love"]]])  # Change based on the context
predicted_word = model.predict(input_context)
print(id_to_word[np.argmax(predicted_word)])
