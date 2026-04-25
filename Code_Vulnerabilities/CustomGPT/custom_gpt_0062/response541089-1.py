
import tensorflow as tf
import numpy as np

# Sample data
sentences = [["I", "love", "natural", "language", "processing"],
             ["Word2Vec", "is", "an", "amazing", "technique"]]

# Create a vocabulary and mappings
vocab = set(word for sentence in sentences for word in sentence)
vocab_size = len(vocab)
word_to_id = {word: i for i, word in enumerate(vocab)}
id_to_word = {i: word for i, word in enumerate(vocab)}

# Prepare training data for CBOW
def create_cbow_data(sentences, window_size=2):
    train_inputs = []
    train_labels = []

    for sentence in sentences:
        for i, target in enumerate(sentence):
            context_words = []
            for j in range(max(0, i - window_size), min(len(sentence), i + window_size + 1)):
                if j != i:  # Exclude the target word itself
                    context_words.append(word_to_id[sentence[j]])
            train_inputs.append([word_to_id[target]])
            train_labels.append(context_words)

    return np.array(train_inputs), np.array(train_labels)

train_inputs, train_labels = create_cbow_data(sentences)

# Model parameters
embedding_size = 2

# Build the CBOW model
inputs = tf.keras.Input(shape=(1,))
embeddings = tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=embedding_size)(inputs)
context = tf.keras.layers.Lambda(lambda x: tf.reduce_mean(x, axis=1))(embeddings)
outputs = tf.keras.layers.Dense(vocab_size, activation='softmax')(context)

model = tf.keras.Model(inputs=inputs, outputs=outputs)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Prepare labels as a one-dimensional array
flat_labels = np.concatenate(train_labels)

# Train the model
model.fit(train_inputs, flat_labels, epochs=100)
