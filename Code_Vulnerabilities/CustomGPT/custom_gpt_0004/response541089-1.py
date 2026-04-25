
import numpy as np
import tensorflow as tf

# Example parameters
vocab_size = 10000  # Size of the vocabulary
embedding_dim = 128  # Dimensionality of the embedding
window_size = 2  # Context window size

# Placeholder for input and output
train_inputs = tf.placeholder(tf.int32, shape=[None, window_size * 2])  # Context words
train_labels = tf.placeholder(tf.int32, shape=[None, 1])  # Target word

# Embedding layer
embeddings = tf.Variable(tf.random_uniform([vocab_size, embedding_dim], -1.0, 1.0))
input_embeds = tf.nn.embedding_lookup(embeddings, train_inputs)

# Average the context embeddings
average_embed = tf.reduce_mean(input_embeds, axis=1)

# Output layer
weights = tf.Variable(tf.truncated_normal([vocab_size, embedding_dim], stddev=0.1))
biases = tf.Variable(tf.zeros([vocab_size]))
logits = tf.matmul(average_embed, weights, transpose_b=True) + biases
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=tf.squeeze(train_labels)))

# Training operation
optimizer = tf.train.AdamOptimizer(learning_rate=0.001)
train_op = optimizer.minimize(loss)

# Example training loop
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    # Insert your training data here
    # train_data should be in the format of context words and target labels
    for epoch in range(num_epochs):
        for batch in train_data:
            context_words, target_word = batch
            feed_dict = {train_inputs: context_words, train_labels: target_word}
            sess.run(train_op, feed_dict=feed_dict)

    # After training, you can retrieve the embeddings
    trained_embeddings = sess.run(embeddings)
