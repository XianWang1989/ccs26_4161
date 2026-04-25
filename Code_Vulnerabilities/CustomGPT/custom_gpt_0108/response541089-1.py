
import tensorflow as tf
import numpy as np

# Sample data: context words and target word
# Assume vocab_size = 5 (for example), with words encoded as integers
context = [[0, 1, 2], [1, 2, 3], [2, 3, 4]]  # Context words (input)
target = [[3], [4], [5]]  # Target words (output)

# Parameters
vocab_size = 6
embedding_size = 2

# Placeholder for inputs and labels
train_inputs = tf.placeholder(tf.int32, shape=[None, 3])  # CBOW inputs (context)
train_labels = tf.placeholder(tf.int32, shape=[None, 1])  # CBOW labels (target word)

# Create embeddings
embeddings = tf.Variable(tf.random_uniform([vocab_size, embedding_size], -1.0, 1.0))

# Look up the embeddings for the context words
input_embeds = tf.nn.embedding_lookup(embeddings, train_inputs)

# Average the embeddings to form the input vector
average_embed = tf.reduce_mean(input_embeds, axis=1)

# Softmax layer
weights = tf.Variable(tf.truncated_normal([embedding_size, vocab_size], stddev=0.1))
biases = tf.Variable(tf.zeros([vocab_size]))
logits = tf.matmul(average_embed, weights) + biases

# Loss function
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=tf.squeeze(train_labels), logits=logits))

# Optimizer
optimizer = tf.train.AdamOptimizer(learning_rate=0.01).minimize(loss)

# Sample training process
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    # Dummy training loop
    for epoch in range(100):
        feed_dict = {train_inputs: np.array(context), train_labels: np.array(target)}
        _, loss_value = sess.run([optimizer, loss], feed_dict=feed_dict)
        print(f'Epoch {epoch}, Loss: {loss_value}')
