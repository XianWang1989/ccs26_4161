
import tensorflow as tf
import numpy as np

# Sample data
sentences = [["hello", "world"], ["my", "name", "is", "chatgpt"]]

# Build vocabulary and mapping
word_to_id = {word: i for i, word in enumerate(set(word for sentence in sentences for word in sentence))}
id_to_word = {i: word for word, i in word_to_id.items()}

# Parameters
embedding_dim = 10
window_size = 1
num_words = len(word_to_id)

# Prepare CBOW training data
train_inputs = []
train_labels = []

for sentence in sentences:
    for i, word in enumerate(sentence):
        # Define the context
        context = []
        for j in range(max(0, i - window_size), min(len(sentence), i + window_size + 1)):
            if j != i:
                context.append(word_to_id[sentence[j]])

        train_inputs.append(context)
        train_labels.append(word_to_id[word])

# Convert to numpy arrays
train_inputs = np.array(train_inputs)
train_labels = np.array(train_labels)

# Build the model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(num_words, embedding_dim, input_length=window_size * 2),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(num_words, activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(train_inputs, train_labels, epochs=100)

# Example prediction
predicted = model.predict(np.array([train_inputs[0]]))
predicted_word = id_to_word[np.argmax(predicted)]
print(f'Predicted word: {predicted_word}')
