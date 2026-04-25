
import tensorflow as tf
import numpy as np

# Parameters
vocab_size = 10000  # Size of the vocabulary
embedding_size = 128  # Embedding size
window_size = 2  # Context window size

# Sample data
train_data = [([1, 2], 3), ([2, 3], 4)]  # List of (context, target)

# Placeholders
train_inputs = tf.placeholder(tf.int32, shape=[None, window_size])  # Context words
train_labels = tf.placeholder(tf.int32, shape=[None, 1])  # Target word

# Embedding layer
embeddings = tf.Variable(tf.random_uniform([vocab_size, embedding_size], -1.0, 1.0))
embed = tf.reduce_mean(tf.nn.embedding_lookup(embeddings, train_inputs), axis=1)

# Output layer
W = tf.Variable(tf.random_uniform([vocab_size, embedding_size], -1.0, 1.0))
b = tf.Variable(tf.zeros([vocab_size]))
logits = tf.matmul(embed, W, transpose_b=True) + b
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=tf.squeeze(train_labels), logits=logits))

# Training operation
optimizer = tf.train.AdamOptimizer(learning_rate=0.01)
train_op = optimizer.minimize(loss)

# Session
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    # Example of training loop
    for step in range(1000):
        x_batch, y_batch = np.array(train_data).T  # Prepare batches
        feed_dict = {train_inputs: x_batch, train_labels: y_batch}
        _, loss_val = sess.run([train_op, loss], feed_dict=feed_dict)

        if step % 100 == 0:
            print(f'Step {step}, Loss: {loss_val}')
