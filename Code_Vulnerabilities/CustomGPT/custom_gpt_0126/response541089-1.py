
import tensorflow as tf
import numpy as np

# Sample data
sentences = [["the", "dog", "barked"], ["the", "cat", "meowed"]]
# Vocabulary creation and preprocessing
vocab = set(word for sentence in sentences for word in sentence)
word_to_index = {word: i for i, word in enumerate(vocab)}
index_to_word = {i: word for word, i in word_to_index.items()}

# Parameters
embedding_dim = 10
window_size = 1

# Create training data for CBOW
train_inputs = []
train_labels = []

for sentence in sentences:
    for index, word in enumerate(sentence):
        context = []
        # Collect context words
        for i in range(max(0, index - window_size), min(len(sentence), index + window_size + 1)):
            if i != index:
                context.append(word_to_index[sentence[i]])

        # Create training pairs
        train_inputs.append(context)
        train_labels.append(word_to_index[word])

# Define model
train_inputs = tf.keras.preprocessing.sequence.pad_sequences(train_inputs, padding='post')
train_labels = np.array(train_labels)

model = tf.keras.Sequential()
model.add(tf.keras.layers.Embedding(input_dim=len(vocab), output_dim=embedding_dim, input_length=train_inputs.shape[1]))
model.add(tf.keras.layers.GlobalAveragePooling1D())
model.add(tf.keras.layers.Dense(len(vocab), activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_inputs, train_labels, epochs=100)
