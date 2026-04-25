
import tensorflow as tf
import numpy as np

# Sample data
words = ["I", "like", "to", "play", "football"]
word2id = {word: i for i, word in enumerate(words)}
id2word = {i: word for i, word in enumerate(words)}

# CBOW input and output
def generate_cbow_data(corpus, window_size=1):
    for i in range(window_size, len(corpus) - window_size):
        context = [corpus[j] for j in range(i - window_size, i + window_size + 1) if j != i]
        target = corpus[i]
        yield context, target

data = list(generate_cbow_data(words))

# Parameters
embedding_dim = 5
vocab_size = len(words)

# CBOW Model
train_inputs = tf.placeholder(tf.int32, shape=[None])
train_labels = tf.placeholder(tf.int32, shape=[None, 1])

embeddings = tf.Variable(tf.random_uniform([vocab_size, embedding_dim], -1.0, 1.0))
input_embeds = tf.nn.embedding_lookup(embeddings, train_inputs)

# Average context embeddings
average_context = tf.reduce_mean(input_embeds, axis=1)

# Output layer
weights = tf.Variable(tf.random_normal([embedding_dim, vocab_size]))
biases = tf.Variable(tf.random_normal([vocab_size]))
logits = tf.matmul(average_context, weights) + biases

# Loss and optimizer
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=train_labels[:, 0], logits=logits))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(loss)

# Training phase
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for epoch in range(1000):
        for context, target in data:
            context_ids = [word2id[w] for w in context]
            target_id = word2id[target]
            feed_dict = {train_inputs: context_ids, train_labels: [[target_id]]}
            sess.run(optimizer, feed_dict=feed_dict)

    # Retrieve the learned embeddings
    learned_embeddings = sess.run(embeddings)
