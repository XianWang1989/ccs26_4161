
import tensorflow as tf
import numpy as np

# Sample data (context and target word)
context_words = [1, 2, 3]  # Example context word indices
target_word = 0  # Target word index

# CBOW: Use context words as inputs and target word as label
train_inputs = np.array(context_words)
train_labels = np.array([target_word])

# Define model parameters
vocab_size = 10  # For example
embedding_dim = 128

# Define the CBOW model
def create_cbow_model(vocab_size, embedding_dim):
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=len(train_inputs)),
        tf.keras.layers.GlobalAveragePooling1D(),
        tf.keras.layers.Dense(vocab_size, activation='softmax')
    ])
    return model

model = create_cbow_model(vocab_size, embedding_dim)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_inputs.reshape(1, -1), train_labels, epochs=10)
