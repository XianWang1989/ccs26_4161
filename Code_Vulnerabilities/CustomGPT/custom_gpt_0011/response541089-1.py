
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# Sample training data
sentences = [
    'the cat sat on the mat',
    'the dog sat on the rug',
    'cats and dogs are great pets'
]

# Tokenization
tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)
total_words = len(tokenizer.word_index) + 1

# Create input and output pairs for CBOW
input_sequences = []
output_words = []
window_size = 1

for sentence in sentences:
    tokenized_sentence = tokenizer.texts_to_sequences([sentence])[0]
    for i in range(window_size, len(tokenized_sentence) - window_size):
        input_sequences.append(tokenized_sentence[i-window_size:i] + tokenized_sentence[i+1:i+window_size+1])
        output_words.append(tokenized_sentence[i])

input_sequences = np.array(input_sequences)
output_words = np.array(output_words)

# One-hot encoding of the output words
output_words = tf.keras.utils.to_categorical(output_words, num_classes=total_words)

# Define CBOW model
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Embedding(input_dim=total_words, output_dim=10, input_length=2 * window_size))
model.add(tf.keras.layers.GlobalAveragePooling1D())
model.add(tf.keras.layers.Dense(10, activation='relu'))
model.add(tf.keras.layers.Dense(total_words, activation='softmax'))

# Compile and train the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(input_sequences, output_words, epochs=100)
