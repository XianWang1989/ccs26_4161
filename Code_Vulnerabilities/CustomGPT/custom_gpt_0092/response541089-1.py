
import numpy as np
import tensorflow as tf

# Sample data: list of sentences
sentences = ["the cat sits on the mat", "the dog barks at the cat"]

# Preprocessing: tokenize the sentences and create a vocabulary
tokenized_sentences = [sentence.split() for sentence in sentences]
vocab = set(word for sentence in tokenized_sentences for word in sentence)
word_to_id = {word: i for i, word in enumerate(vocab)}
id_to_word = {i: word for word, i in word_to_id.items()}

# Parameters
embedding_dim = 10
window_size = 2

# Create training data
train_inputs = []
train_labels = []

for sentence in tokenized_sentences:
    for i, word in enumerate(sentence):
        # Generate context words
        context = []
        for j in range(max(0, i - window_size), min(len(sentence), i + window_size + 1)):
            if j != i:  # Skip the target word
                context.append(word_to_id[sentence[j]])
        train_inputs.append(context)
        train_labels.append(word_to_id[word])  # CBOW: Input is context, label is target

# Convert to numpy arrays
train_inputs = np.array(train_inputs)
train_labels = np.array(train_labels)

# Define the model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(len(vocab), embedding_dim, input_length=window_size * 2),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(len(vocab), activation='softmax')
])

# Compile the model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')

# Train the model
model.fit(train_inputs, train_labels, epochs=100)

# Example prediction
word_index = word_to_id['cat']
predicted = model.predict(np.array([train_inputs[0]]))  # Example input
predicted_word = id_to_word[np.argmax(predicted)]
print(f"Predicted word for context {train_inputs[0]}: {predicted_word}")
