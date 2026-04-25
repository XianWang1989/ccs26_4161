
import tensorflow as tf
import numpy as np

# Example data: context words (input) and target words (labels)
def generate_cbow_data(corpus, window_size):
    inputs = []
    labels = []

    for i in range(window_size, len(corpus) - window_size):
        context = corpus[i-window_size:i] + corpus[i+1:i+window_size+1]
        target = corpus[i]
        inputs.append(context)
        labels.append(target)

    return np.array(inputs), np.array(labels)

# Dummy corpus
corpus = ['I', 'love', 'to', 'learn', 'machine', 'learning', 'and', 'tensorflow']
window_size = 2

# Generate CBOW data
train_inputs, train_labels = generate_cbow_data(corpus, window_size)

# Create the TensorFlow model
vocab_size = len(set(corpus))
embedding_dim = 128

# Input layer
inputs = tf.keras.Input(shape=(window_size * 2,), dtype=tf.int32)
embedding_layer = tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=embedding_dim)(inputs)
output_layer = tf.keras.layers.GlobalAveragePooling1D()(embedding_layer)
output_layer = tf.keras.layers.Dense(vocab_size, activation='softmax')(output_layer)

model = tf.keras.Model(inputs=inputs, outputs=output_layer)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_inputs, train_labels, epochs=10)
