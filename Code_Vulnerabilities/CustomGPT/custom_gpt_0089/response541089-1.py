
import tensorflow as tf
import numpy as np

# Sample data: context words and corresponding target words
context_words = [[1, 2], [2, 3], [3, 4]]  # Context (input)
target_words = [0, 1, 2]                   # Target (labels)

# Parameters
embedding_size = 10  # Size of word embeddings
vocab_size = 5       # Number of unique words
learning_rate = 0.01

# Placeholders for input and output
train_inputs = tf.placeholder(tf.int32, shape=[None])  # Context words
train_labels = tf.placeholder(tf.int32, shape=[None, 1])  # Target words

# Embedding layer
embeddings = tf.Variable(tf.random_uniform([vocab_size, embedding_size], -1.0, 1.0))

# Look up embeddings for context words
embed = tf.nn.embedding_lookup(embeddings, train_inputs)

# CBOW: Averaging context word embeddings
context_mean = tf.reduce_mean(embed, axis=1)

# Softmax layer for classification of target words
weights = tf.Variable(tf.truncated_normal([embedding_size, vocab_size]))
biases = tf.Variable(tf.zeros([vocab_size]))

# Output layer
logits = tf.matmul(context_mean, weights) + biases
loss = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=tf.squeeze(train_labels))
optimizer = tf.train.AdamOptimizer(learning_rate).minimize(loss)

# Training
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for epoch in range(1000):
        feed_dict = {train_inputs: np.array(context_words).flatten(), 
                     train_labels: np.array(target_words).reshape(-1, 1)}

        _, loss_value = sess.run([optimizer, loss], feed_dict=feed_dict)

        if epoch % 100 == 0:
            print(f'Epoch {epoch}, Loss: {loss_value.mean()}')

    # Extract learned embeddings
    learned_embeddings = sess.run(embeddings)
    print("Learned embeddings:", learned_embeddings)
