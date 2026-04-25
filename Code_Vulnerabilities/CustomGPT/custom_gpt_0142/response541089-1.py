
import tensorflow as tf
import numpy as np

# Sample data: List of sentences
sentences = [["i", "love", "coding"], ["coding", "is", "fun"], ["i", "enjoy", "learning"]]

# Build a vocabulary
words = list(set(word for sentence in sentences for word in sentence))
word_to_index = {word: i for i, word in enumerate(words)}
index_to_word = {i: word for i, word in enumerate(words)}
vocab_size = len(words)

# Function to generate training data for CBOW
def generate_cbow_data(sentences, window_size=1):
    training_data = []
    for sentence in sentences:
        for i in range(len(sentence)):
            context = []
            target = sentence[i]
            # Get context words within the window_size
            for j in range(max(0, i - window_size), min(len(sentence), i + window_size + 1)):
                if j != i:  # Exclude target word
                    context.append(word_to_index[sentence[j]])
            # Append the context and corresponding target
            training_data.append((context, word_to_index[target]))
    return training_data

# Create training data
training_data = generate_cbow_data(sentences)

# Prepare inputs and labels
train_inputs = np.array([np.array(context) for context, _ in training_data])
train_labels = np.array([label for _, label in training_data])

# Define model parameters
embedding_dim = 50

# Create tensors for inputs and labels
inputs = tf.placeholder(tf.int32, shape=[None, None])  # Context word indices
labels = tf.placeholder(tf.int32, shape=[None])  # Target word indices

# Create an embedding matrix
embeddings = tf.Variable(tf.random_uniform([vocab_size, embedding_dim], -1.0, 1.0))

# Look up the embeddings for the input context words
context_embeddings = tf.nn.embedding_lookup(embeddings, inputs)

# Average the context embeddings
average_context = tf.reduce_mean(context_embeddings, axis=1)

# Define weights and bias for the output layer
weights = tf.Variable(tf.random_normal([embedding_dim, vocab_size]))
bias = tf.Variable(tf.zeros([vocab_size]))

# Compute logits and predictions
logits = tf.matmul(average_context, weights) + bias
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(
    labels=labels, logits=logits))

# Optimizer
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(loss)

# Start the TensorFlow session
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    # Training loop (pseudo-code)
    for epoch in range(100):
        # Feed input data
        feed_dict = {inputs: train_inputs, labels: train_labels}
        _, curr_loss = sess.run([optimizer, loss], feed_dict=feed_dict)
        print(f'Epoch {epoch}, Loss: {curr_loss}')
