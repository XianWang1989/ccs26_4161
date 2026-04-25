
import tensorflow as tf
import numpy as np
from collections import Counter

# Prepare your data
def generate_training_data(corpus, window_size):
    training_inputs = []
    training_labels = []

    for sentence in corpus:
        words = sentence.split()
        for i, word in enumerate(words):
            # Create a context window
            context = words[max(0, i - window_size): i] + words[i + 1: min(len(words), i + window_size + 1)]
            for context_word in context:
                training_inputs.append(word)      # Target word
                training_labels.append(context_word)  # Context word

    return training_inputs, training_labels

# Example corpus
corpus = ["the cat sat on the mat", "the dog sat on the log"]
window_size = 2
inputs, labels = generate_training_data(corpus, window_size)

# Create vocabulary
word_counts = Counter(inputs + labels)
vocab = {word: i for i, (word, _) in enumerate(word_counts.items())}
vocab_size = len(vocab)

# Convert words to indices
input_indices = [vocab[word] for word in inputs]
label_indices = [vocab[word] for word in labels]

# Parameters
embedding_size = 128  # Size of the embedding vector
learning_rate = 0.01

# Build the CBOW model
train_inputs = tf.placeholder(tf.int32, shape=[None])
train_labels = tf.placeholder(tf.int32, shape=[None])

# Embedding layer
embeddings = tf.Variable(tf.random_uniform([vocab_size, embedding_size], -1.0, 1.0))
input_embeds = tf.nn.embedding_lookup(embeddings, train_inputs)

# Average the embedded input
input_avg = tf.reduce_mean(input_embeds, axis=1)

# Output layer
weights = tf.Variable(tf.random_normal([embedding_size, vocab_size]))
biases = tf.Variable(tf.random_normal([vocab_size]))

logits = tf.matmul(input_avg, weights) + biases
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=train_labels))

# Training operation
optimizer = tf.train.GradientDescentOptimizer(learning_rate)
train_op = optimizer.minimize(loss)

# Train the model
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(100):  # Example: train for 100 epochs
        sess.run(train_op, feed_dict={train_inputs: input_indices, train_labels: label_indices})
        if epoch % 10 == 0:
            print(f'Epoch {epoch}, Loss: {sess.run(loss, feed_dict={train_inputs: input_indices, train_labels: label_indices})}')

print("Training complete!")
