
import tensorflow as tf
import numpy as np

# Parameters
vocabulary_size = 10000  # Size of the vocabulary
embedding_size = 128     # Dimension of the embedding
window_size = 2          # Context window size
train_data = [...]       # Your training data

# Prepare your CBOW training data (context words and target word)
def prepare_data(train_data):
    inputs = []
    labels = []
    for sentence in train_data:
        for index, word in enumerate(sentence):
            context = []
            for w in range(-window_size, window_size + 1):
                if w != 0 and 0 <= index + w < len(sentence):
                    context.append(sentence[index + w])
            # Prepare input and label
            inputs.append(context)
            labels.append(word)
    return np.array(inputs), np.array(labels)

train_inputs, train_labels = prepare_data(train_data)

# Create the model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocabulary_size, embedding_size, input_length=window_size*2),
    tf.keras.layers.Lambda(lambda x: tf.reduce_mean(x, axis=1)),  # Average the embeddings
    tf.keras.layers.Dense(vocabulary_size, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_inputs, train_labels, epochs=10, batch_size=64)

# Save the model
model.save('cbow_word2vec_model.h5')
