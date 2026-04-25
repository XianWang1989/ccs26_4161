
import numpy as np
import tensorflow as tf

# Sample data: a small vocabulary and a simple context/target example
vocabulary = ['word1', 'word2', 'word3', 'word4']
word_to_id = {word: idx for idx, word in enumerate(vocabulary)}
id_to_word = {idx: word for idx, word in enumerate(vocabulary)}

# Sample context and target
context = ['word1', 'word2']  # context words
target = 'word3'  # target word

# Prepare training data
train_inputs = np.array([word_to_id[word] for word in context])
train_labels = np.array([word_to_id[target]])

# Build the CBOW model
embedding_dim = 128
vocab_size = len(vocabulary)

# Placeholder for inputs (context)
inputs = tf.placeholder(tf.int32, shape=[None])

# Embeddings
embeddings = tf.Variable(tf.random_uniform([vocab_size, embedding_dim], -1.0, 1.0))
embed = tf.nn.embedding_lookup(embeddings, inputs)

# Combine embeddings
mean_embed = tf.reduce_mean(embed, axis=0)

# Softmax weights and biases
softmax_weights = tf.Variable(tf.truncated_normal([vocab_size, embedding_dim], stddev=0.1))
softmax_biases = tf.Variable(tf.zeros([vocab_size]))

# Calculate logits and loss
logits = tf.matmul(mean_embed, tf.transpose(softmax_weights)) + softmax_biases
labels = tf.placeholder(tf.int32, shape=[None])
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=labels, logits=logits))

# Optimizer
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
train_op = optimizer.minimize(loss)

# Run the model
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    feed_dict = {inputs: train_inputs, labels: train_labels}
    for epoch in range(1000):  # Example epochs
        sess.run(train_op, feed_dict=feed_dict)

    # Extract trained embeddings
    trained_embeddings = sess.run(embeddings)
    print("Trained embeddings:\n", trained_embeddings)
