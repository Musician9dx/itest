import tensorflow as tf


def get_device():
    try:

        tpu = tf.distribute.cluster_resolver.TPUClusterResolver.connect()

        strategy = tf.distribute.TPUStrategy(tpu)
        print(f'꧁ Running on TPU ꧂', tpu.master(), end=' | ')

        print('Num of TPUs: ', strategy.num_replicas_in_sync)
        device = "TPU"
    except:

        gpus = tf.config.list_logical_devices('GPU')
        ngpu = len(gpus)

        if ngpu:

            strategy = tf.distribute.MirroredStrategy(gpus)

            print("꧁ Running on GPU ꧂", end=' | ')

            print("Num of GPUs: ", ngpu)
            device = 'GPU'
        else:

            print("꧁ Running on CPU ꧂")

            strategy = tf.distribute.get_strategy()
            device = 'CPU'


