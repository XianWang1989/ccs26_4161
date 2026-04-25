
import tensorflow as tf
import numpy as np

# Sample data
sentences = ["the quick brown fox jumps over the lazy dog"]
words = [word for sentence in sentences for word in sentence.split()]
word_set = set(words)
word_to_index = {word: i for i, word in enumerate(word_set)}
index_to_word = {i: word for i, word in enumerate(word_set)}

# Parameters
vector_size = 8
window_size = 2
learning_rate = 0.01

# Preparing training data
train_inputs = []
train_labels = []

for i, word in enumerate(words):
    # Context words
    context = words[max(0, i - window_size):i] + words[i + 1:min(len(words), i + window_size + 1)]
    for target in context:
        train_inputs.append(word_to_index[target])
        train_labels.append(word_to_index[word])

# Creating the CBOW model
input_layer = tf.keras.layers.Input(shape=(1,))
embedding_layer = tf.keras.layers.Embedding(len(word_set), vector_size)(input_layer)
avg_layer = tf.keras.layers.Lambda(lambda x: tf.reduce_mean(x, axis=1))(embedding_layer)
output_layer = tf.keras.layers.Dense(len(word_set), activation='softmax')(avg_layer)

model = tf.keras.models.Model(inputs=input_layer, outputs=output_layer)
model.compile(loss='sparse_categorical_crossentropy', optimizer=tf.keras.optimizers.Adam(learning_rate))

# Converting to numpy arrays
train_inputs = np.array(train_inputs)
train_labels = np.array(train_labels)

# Training the model
model.fit(train_inputs, train_labels, epochs=100)

# Example prediction
predicted = model.predict(np.array([[word_to_index['the']]]))
predicted_word = index_to_word[np.argmax(predicted)]
print(f"Predicted word for 'the': {predicted_word}")
