
import numpy as np
import tensorflow as tf

# Parameters
vocab_size = 10000  # Adjust the size as needed
embedding_size = 128  # Dimension of the embedding vector
window_size = 2  # Context window size
num_sampled = 64  # Number of negative samples

# Placeholder for inputs (context words) and labels (target words)
train_inputs = tf.placeholder(tf.int32, shape=[None, window_size * 2])
train_labels = tf.placeholder(tf.int32, shape=[None, 1])

# Embedding layer
embeddings = tf.Variable(tf.random_uniform([vocab_size, embedding_size], -1.0, 1.0))
input_embeds = tf.nn.embedding_lookup(embeddings, train_inputs)

# CBOW: Average the context word embeddings
context_embeds = tf.reduce_mean(input_embeds, axis=1)

# Output layer weights and biases
weights = tf.Variable(tf.truncated_normal([vocab_size, embedding_size], stddev=1.0 / np.sqrt(embedding_size)))
biases = tf.Variable(tf.zeros([vocab_size]))

# Compute logits and loss
logits = tf.matmul(context_embeds, tf.transpose(weights)) + biases
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=tf.reshape(train_labels, [-1])))

# Training operation
optimizer = tf.train.AdamOptimizer(learning_rate=0.01)
train_op = optimizer.minimize(loss)

# Session to run the graph
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    # Feed in your training data here
    for step in range(10000):  # Number of epochs
        batch_inputs, batch_labels = ...  # Prepare your batches
        feed_dict = {train_inputs: batch_inputs, train_labels: batch_labels}
        _, current_loss = sess.run([train_op, loss], feed_dict=feed_dict)

        if step % 1000 == 0:
            print(f'Step: {step}, Loss: {current_loss}')

# After training, embeddings can be accessed from 'embeddings' variable.
