
import tensorflow as tf
import numpy as np
import random

# Sample data for CBOW
def create_dataset(corpus, window_size=2):
    inputs, labels = [], []
    for sentence in corpus:
        words = sentence.split()
        for i, word in enumerate(words):
            context = []
            for j in range(max(0, i - window_size), min(len(words), i + window_size + 1)):
                if i != j:
                    context.append(words[j])
            if context:
                inputs.append(context)
                labels.append(word)
    return inputs, labels

# Hyperparameters
embedding_size = 100
vocabulary_size = 1000
window_size = 2
learning_rate = 0.01
epochs = 1000

# Sample corpus
corpus = [
    'the quick brown fox',
    'jumped over the lazy dog',
    'the dog barked'
]

# Create training data
train_inputs, train_labels = create_dataset(corpus, window_size)
train_inputs = tf.keras.preprocessing.text.Tokenizer()
train_inputs.fit_on_texts(train_inputs)
train_labels = tf.keras.preprocessing.text.Tokenizer()
train_labels.fit_on_texts(train_labels)

# Prepare the data
train_inputs = np.array(train_inputs.texts_to_sequences(train_inputs))
train_labels = np.array(train_labels.texts_to_sequences(train_labels)).flatten()

# Build model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocabulary_size, embedding_size, input_length=window_size * 2),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(vocabulary_size, activation='softmax')
])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train model
model.fit(train_inputs, train_labels, epochs=epochs)

# Example output function
def get_word_vector(word):
    index = train_labels.word_index.get(word)
    if index is not None:
        return model.layers[0].get_weights()[0][index]
    return None

# Testing the function
print(get_word_vector('the'))
