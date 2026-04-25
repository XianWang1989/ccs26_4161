
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical

# Sample data
corpus = [
    'I love to play football',
    'I love to watch movies',
    'I enjoy playing video games',
    'Football is a great sport'
]

# Tokenization
tokenizer = Tokenizer()
tokenizer.fit_on_texts(corpus)
total_words = len(tokenizer.word_index) + 1

# Create CBOW training data
def create_cbow_data(corpus, window_size):
    input_words, target_words = [], []
    for line in corpus:
        tokenized_line = tokenizer.texts_to_sequences([line])[0]
        for i in range(window_size, len(tokenized_line) - window_size):
            input_words.append(tokenized_line[i - window_size:i + window_size])
            target_words.append(tokenized_line[i])
    return np.array(input_words), np.array(target_words)

window_size = 2
X, y = create_cbow_data(corpus, window_size)
y = to_categorical(y, num_classes=total_words)

# Define the CBOW model
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Embedding(total_words, 10, input_length=window_size * 2))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(total_words, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=100, verbose=1)

# Check model summary
model.summary()
