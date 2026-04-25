
import tensorflow as tf
import numpy as np

# Sample data
context_words = [['the', 'cat', 'sits'], ['the', 'dog', 'barks']]
target_words = ['sits', 'barks']

# Create a vocabulary and mapping
vocab = list(set(word for sentence in context_words for word in sentence) | set(target_words))
word_to_index = {word: idx for idx, word in enumerate(vocab)}

def generate_cbow_data(context, target):
    context_indices = [word_to_index[word] for word in context]
    target_index = word_to_index[target]
    return context_indices, target_index

# Preparing the training data
train_inputs, train_labels = zip(*[generate_cbow_data(context, target) for context, target in zip(context_words, target_words)])

# Convert to NumPy arrays
train_inputs = np.array(train_inputs)
train_labels = np.array(train_labels)

# CBOW model
embedding_size = 128
vocabulary_size = len(vocab)

# Input placeholders
X = tf.placeholder(tf.int32, shape=[None, None])  # Input context
y = tf.placeholder(tf.int32, shape=[None])        # Target word

# Embedding layer
embeddings = tf.Variable(tf.random_uniform([vocabulary_size, embedding_size], -1.0, 1.0))
input_embeds = tf.reduce_mean(tf.nn.embedding_lookup(embeddings, X), axis=1)

# Softmax weights and biases
weights = tf.Variable(tf.truncated_normal([embedding_size, vocabulary_size], stddev=0.1))
biases = tf.Variable(tf.zeros([vocabulary_size]))

# Model output
logits = tf.matmul(input_embeds, weights) + biases
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=y))

# Optimizer
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(loss)

# Training session
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    # Example training loop
    for epoch in range(100):  # Adjust epochs as needed
        feed_dict = {X: train_inputs, y: train_labels}
        _, loss_value = sess.run([optimizer, loss], feed_dict=feed_dict)
        print(f'Epoch {epoch}, Loss: {loss_value}')
