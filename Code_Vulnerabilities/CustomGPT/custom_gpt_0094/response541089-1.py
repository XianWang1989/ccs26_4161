
import tensorflow as tf
import numpy as np

# Sample data
sentences = [
    "the cat sits on the mat",
    "the dog barks at the cat"
]

# Preprocessing the data: tokenization and vocabulary creation
tokenized_sentences = [sentence.split() for sentence in sentences]
vocab = set(word for sentence in tokenized_sentences for word in sentence)
vocab_size = len(vocab)
word_to_idx = {word: i for i, word in enumerate(vocab)}

# Function to create training data for CBOW
def create_cbow_data(sentences, window_size=2):
    input_words = []
    target_words = []

    for sentence in sentences:
        for i, target in enumerate(sentence):
            context = []
            # Get context words within window size
            for j in range(max(0, i - window_size), min(len(sentence), i + window_size + 1)):
                if j != i:  # Exclude the target word
                    context.append(word_to_idx[sentence[j]])
            input_words.append(context)
            target_words.append(word_to_idx[target])

    return input_words, target_words

# Creating the training data
input_words, target_words = create_cbow_data(tokenized_sentences)

# Parameters
embedding_dim = 10
num_samples = len(input_words)

# Defining the model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=2*2),  # 2*window_size
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(vocab_size, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Preparing the data for training
input_words = tf.keras.preprocessing.sequence.pad_sequences(input_words, padding='post')

# Fitting the model
model.fit(input_words, np.array(target_words), epochs=100)

# Now the model is trained using the CBOW architecture!
