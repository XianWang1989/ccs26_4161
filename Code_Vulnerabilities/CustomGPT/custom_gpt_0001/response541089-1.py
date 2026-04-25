
import tensorflow as tf
import numpy as np

# Sample data
# Assuming you have tokenized your text and converted words to indices
data = [1, 2, 3, 4, 5]  # Example word indices
window_size = 2  # Number of context words to consider

# Creating training data for CBOW
def create_cbow_data(data, window_size):
    train_inputs = []
    train_labels = []

    for i in range(window_size, len(data) - window_size):
        context = data[i - window_size:i] + data[i + 1:i + window_size + 1]
        target = data[i]

        train_inputs.append(context)
        train_labels.append(target)

    return np.array(train_inputs), np.array(train_labels)

train_inputs, train_labels = create_cbow_data(data, window_size)

# Parameters
vocabulary_size = 6  # number of unique words
embedding_size = 128  # dimension of the embedding

# Define the model
class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim):
        super(CBOWModel, self).__init__()
        self.embeddings = tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=2 * window_size)

    def call(self, inputs):
        embedded = self.embeddings(inputs)
        return tf.reduce_mean(embedded, axis=1)  # Mean of the context embeddings

cbow_model = CBOWModel(vocabulary_size, embedding_size)

# Output layer
output_layer = tf.keras.layers.Dense(vocabulary_size, activation='softmax')

# Complete model
inputs = tf.keras.Input(shape=(2 * window_size,))
embeddings = cbow_model(inputs)
outputs = output_layer(embeddings)

model = tf.keras.Model(inputs, outputs)

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_inputs, train_labels, epochs=100)

# You can now use the trained model to get word embeddings or make predictions.
