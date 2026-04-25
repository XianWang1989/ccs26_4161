
import tensorflow as tf
import numpy as np

# Sample data
sentences = [['the', 'cat', 'sat'], ['the', 'dog', 'barked']]
# Create a vocabulary
vocab = set(word for sentence in sentences for word in sentence)
word_to_id = {word: idx for idx, word in enumerate(vocab)}

# Prepare training data for CBOW
train_inputs = []
train_labels = []

window_size = 1  # Context window size
for sentence in sentences:
    for i in range(len(sentence)):
        context = []
        if i >= window_size:
            context.append(word_to_id[sentence[i - window_size]])
        if i + window_size < len(sentence):
            context.append(word_to_id[sentence[i + window_size]])

        train_inputs.append(context)
        train_labels.append(word_to_id[sentence[i]])

# Parameters
vocab_size = len(vocab)
embedding_dim = 10  # Size of the embedding vectors

# Define the model
inputs = tf.keras.layers.Input(shape=(None,))
embeddings = tf.keras.layers.Embedding(vocab_size, embedding_dim)(inputs)
output = tf.keras.layers.Lambda(lambda x: tf.reduce_mean(x, axis=1))(embeddings)  # Average the context embeddings
output = tf.keras.layers.Dense(vocab_size, activation='softmax')(output)

model = tf.keras.models.Model(inputs=inputs, outputs=output)
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')

# Convert the training data to numpy arrays
train_inputs_np = np.array(train_inputs)
train_labels_np = np.array(train_labels)

# Train the model
model.fit(train_inputs_np, train_labels_np, epochs=100)

# Now you can use the model to get word vectors
word_vectors = model.layers[1].get_weights()[0]
