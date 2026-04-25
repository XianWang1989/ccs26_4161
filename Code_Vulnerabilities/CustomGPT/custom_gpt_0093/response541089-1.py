
import tensorflow as tf
import numpy as np

# Sample data
words = ["example", "text", "for", "word2vec", "cbow"]
word_to_id = {word: i for i, word in enumerate(words)}

# Parameters
vocab_size = len(words)
embedding_dim = 2
window_size = 2

# Generate training data for CBOW
def generate_cbow_data(corpus, window_size):
    input_data = []
    label_data = []

    for i in range(window_size, len(corpus) - window_size):
        context = [corpus[i + offset] for offset in range(-window_size, window_size + 1) if offset != 0]
        input_data.append([word_to_id[word] for word in context])
        label_data.append(word_to_id[corpus[i]])

    return np.array(input_data), np.array(label_data)

corpus = ["example", "text", "for", "word2vec", "cbow"]
input_data, label_data = generate_cbow_data(corpus, window_size)

# Model setup
train_inputs = tf.placeholder(tf.int32, shape=[None, window_size * 2])
train_labels = tf.placeholder(tf.int32, shape=[None])

embeddings = tf.Variable(tf.random_uniform([vocab_size, embedding_dim], -1.0, 1.0))
input_embeddings = tf.nn.embedding_lookup(embeddings, train_inputs)
mean_input = tf.reduce_mean(input_embeddings, axis=1)

weights = tf.Variable(tf.random_uniform([embedding_dim, vocab_size], -1.0, 1.0))
biases = tf.Variable(tf.zeros([vocab_size]))

logits = tf.matmul(mean_input, weights) + biases
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=train_labels, logits=logits))

# Training
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train_op = optimizer.minimize(loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    # Train your model here
    # for epoch in range(num_epochs):
    #     sess.run(train_op, feed_dict={train_inputs: input_data, train_labels: label_data})

    # Example to get the embeddings
    final_embeddings = sess.run(embeddings)
