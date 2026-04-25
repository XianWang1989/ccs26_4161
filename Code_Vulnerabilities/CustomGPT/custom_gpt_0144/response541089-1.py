import tensorflow as tf
import numpy as np

# Let's assume you have a vocabulary size of 10
vocabulary_size = 10
embedding_size = 5  # Dimension of the embedding
num_sampled = 3  # Number of negative samples for the noise-contrastive estimation

# CBOW Model
# Train data: 3 context words, target word
context_words = np.array([[1, 2, 3]])  # Example: context words (3 words as input)
target_word = np.array([4])  # Example: target word (1 word as label)

# Placeholders for input and output
train_inputs = tf.placeholder(tf.int32, shape=[None])
train_labels = tf.placeholder(tf.int32, shape=[None, 1])

# Embedding matrix for words
embeddings = tf.Variable(
    tf.random_uniform([vocabulary_size, embedding_size], -1.0, 1.0)
)

# Lookup the embeddings for the context words (CBOW model)
context_embed = tf.nn.embedding_lookup(embeddings, train_inputs)

# Reduce the context word embeddings to a single vector by averaging
context_mean = tf.reduce_mean(context_embed, 0)

# Variables for the weights and biases for the output layer
softmax_weights = tf.Variable(
    tf.random_uniform([vocabulary_size, embedding_size], -1.0, 1.0)
)
softmax_biases = tf.Variable(tf.zeros([vocabulary_size]))

# Compute the logits
logits = tf.matmul(context_mean, tf.transpose(softmax_weights)) + softmax_biases
loss = tf.reduce_mean(
    tf.nn.nce_loss(
        weights=softmax_weights,
        biases=softmax_biases,
        labels=train_labels,
        inputs=context_mean,
        num_sampled=num_sampled,
        num_classes=vocabulary_size
    )
)

# Optimizer to minimize the loss
optimizer = tf.train.GradientDescentOptimizer(learning_rate=1.0)
train_op = optimizer.minimize(loss)

# Initialize TensorFlow session and train
