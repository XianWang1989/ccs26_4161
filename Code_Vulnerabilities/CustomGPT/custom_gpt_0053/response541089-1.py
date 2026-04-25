
import numpy as np
import tensorflow as tf

# Sample data: context (input words) and target (the word to predict)
context_words = [['i', 'love', 'to'], ['love', 'to', 'play'], ['to', 'play', 'football']]
target_words = ['play', 'football', 'soccer']

# Create a vocabulary
vocab = set([word for context in context_words for word in context] + target_words)
vocab_size = len(vocab)
word_to_id = {word: idx for idx, word in enumerate(vocab)}
id_to_word = {idx: word for word, idx in word_to_id.items()}

# Prepare training data
train_inputs = []
train_labels = []
for context, target in zip(context_words, target_words):
    train_inputs.append([word_to_id[w] for w in context])
    train_labels.append(word_to_id[target])

# Convert to arrays
train_inputs = np.array(train_inputs)
train_labels = np.array(train_labels)

# Hyperparameters
embedding_dim = 128
num_epochs = 1000

# Build the CBOW model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=len(train_inputs[0])),
    tf.keras.layers.Dense(vocab_size, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_inputs, train_labels, epochs=num_epochs)

# Example usage
def predict_word(context):
    context_ids = np.array([word_to_id[w] for w in context]).reshape(1, -1)
    prediction = model.predict(context_ids)
    predicted_word_id = np.argmax(prediction, axis=1)
    return id_to_word[predicted_word_id[0]]

# Predict a word given a context
print(predict_word(['i', 'love', 'to']))
