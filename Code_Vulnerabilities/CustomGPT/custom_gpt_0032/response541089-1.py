
import tensorflow as tf
import numpy as np

# Sample data
sentences = [
    "the quick brown fox jumps",
    "over the lazy dog"
]

# Preprocess the data: create a vocabulary
words = " ".join(sentences).split()
vocab = set(words)
word_to_id = {word: i for i, word in enumerate(vocab)}
id_to_word = {i: word for i, word in enumerate(vocab)}

# Hyperparameters
window_size = 2
embedding_dim = 10

# Prepare training data
train_inputs = []
train_labels = []

for sentence in sentences:
    words = sentence.split()
    for i, word in enumerate(words):
        context_words = []

        # Get context words within the window size
        for j in range(max(0, i - window_size), min(len(words), i + window_size + 1)):
            if j != i:
                context_words.append(word_to_id[words[j]])

        # Create CBOW input (context words) and label (target word)
        train_inputs.append(context_words)
        train_labels.append(word_to_id[word])

# Parameters for the model
train_inputs = tf.keras.preprocessing.sequence.pad_sequences(train_inputs, padding='post')
train_labels = np.array(train_labels)

# Building the CBOW model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(len(vocab), embedding_dim, input_length=train_inputs.shape[1]),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(len(vocab), activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_inputs, train_labels, epochs=100)

# Example usage
context = ["the", "quick"]
context_ids = [word_to_id[word] for word in context]
context_ids = tf.keras.preprocessing.sequence.pad_sequences([context_ids], maxlen=train_inputs.shape[1], padding='post')

predicted_word_id = np.argmax(model.predict(context_ids), axis=-1)
print(f"Predicted word: {id_to_word[predicted_word_id[0]]}")
