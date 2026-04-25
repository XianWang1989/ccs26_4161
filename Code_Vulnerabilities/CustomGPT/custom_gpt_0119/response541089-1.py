
import tensorflow as tf
import numpy as np

# Sample dataset
sentences = [["the", "cat", "sat", "on", "the", "mat"]]
# Build your vocabulary
vocab = set(word for sentence in sentences for word in sentence)
word_to_id = {word: i for i, word in enumerate(vocab)}

# Prepare training data for CBOW
def create_cbow_data(sentences, window_size=1):
    train_inputs = []
    train_labels = []
    for sentence in sentences:
        for i, word in enumerate(sentence):
            context = []
            for j in range(-window_size, window_size + 1):
                if j != 0 and 0 <= i + j < len(sentence):
                    context.append(word_to_id[sentence[i + j]])
            train_inputs.append(context)
            train_labels.append(word_to_id[word])
    return np.array(train_inputs), np.array(train_labels)

train_inputs, train_labels = create_cbow_data(sentences)

# Build the CBOW model
vocab_size = len(vocab)
embedding_dim = 128

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=train_inputs.shape[1]),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(vocab_size, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_inputs, train_labels, epochs=10)
