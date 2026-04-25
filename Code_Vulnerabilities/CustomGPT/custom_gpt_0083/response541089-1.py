
import tensorflow as tf
import numpy as np

# Sample data for CBOW
def generate_data(corpus, window_size):
    train_inputs, train_labels = [], []
    for sentence in corpus:
        words = sentence.split()
        for i in range(len(words)):
            context = []
            for j in range(max(0, i-window_size), min(len(words), i+window_size+1)):
                if j != i:
                    context.append(words[j])
            train_inputs.append(context)
            train_labels.append(words[i])
    return train_inputs, train_labels

# Sample corpus
corpus = ["the cat sat on the mat", "the dog sat on the log"]
window_size = 2
train_inputs, train_labels = generate_data(corpus, window_size)

# Prepare vocabulary
vocab = set(word for sentence in train_inputs for word in sentence) | set(train_labels)
word_to_index = {word: i for i, word in enumerate(vocab)}
index_to_word = {i: word for word, i in word_to_index.items()}

# Convert words to indices
train_inputs_idx = [[word_to_index[word] for word in context] for context in train_inputs]
train_labels_idx = [word_to_index[label] for label in train_labels]

# Example parameters
vocab_size = len(vocab)
embedding_dim = 50

# CBOW Model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=window_size * 2),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(vocab_size, activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Prepare input data in correct shape
X = tf.keras.preprocessing.sequence.pad_sequences(train_inputs_idx, padding='pre', maxlen=window_size * 2)
y = np.array(train_labels_idx)

# Train the model
model.fit(X, y, epochs=100, verbose=1)

# Example prediction
predicted_index = np.argmax(model.predict(X[0:1]), axis=-1)
predicted_word = index_to_word[predicted_index[0]]
print(f"Predicted word: {predicted_word}")
