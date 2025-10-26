import tensorflow as tf
print("TF version:", tf.__version__)
print("GPUs:", tf.config.list_physical_devices("GPU"))

with tf.device("/GPU:0"):
    a = tf.random.normal([3000, 3000])
    b = tf.random.normal([3000, 3000])
    c = tf.matmul(a, b)

    print("Matmul done, result shape:", c.shape)
