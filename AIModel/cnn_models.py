import efficientnet.tfkeras as efn
import tensorflow as tf
from keras import Model
from keras.layers import Dropout, Dense, BatchNormalization


class VGG19(Model):
    def __init__(self):
        super(VGG19, self).__init__()
        self.net = tf.keras.applications.VGG19(
            weights=None,
            # weights="./checkpoint/vgg19_weights_tf_dim_ordering_tf_kernels_notop.h5",
            include_top=False,
            pooling="max"
        )
        self.net.trainable = False
        self.f1 = Dense(1024, activation="relu")
        self.b1 = BatchNormalization()
        self.d1 = Dropout(0.5)
        self.f2 = Dense(21, activation="softmax")

    def call(self, x):
        x = self.net(x)
        x = self.f1(x)
        x = self.b1(x)
        x = self.d1(x)
        y = self.f2(x)
        return y


class InceptionV3(Model):
    def __init__(self):
        super(InceptionV3, self).__init__()
        self.net = tf.keras.applications.InceptionV3(
            weights=None,
            # weights="./checkpoint/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5",
            include_top=False,
            pooling="max"
        )
        self.net.trainable = False
        self.f1 = Dense(1024, activation="relu")
        self.b1 = BatchNormalization()
        self.d1 = Dropout(0.5)
        self.f2 = Dense(21, activation="softmax")

    def call(self, x):
        x = self.net(x)
        x = self.f1(x)
        x = self.b1(x)
        x = self.d1(x)
        y = self.f2(x)
        return y


class DenseNet121(Model):
    def __init__(self):
        super(DenseNet121, self).__init__()
        self.net = tf.keras.applications.DenseNet121(
            weights=None,
            # weights="./checkpoint/densenet121_weights_tf_dim_ordering_tf_kernels_notop.h5",
            include_top=False,
            pooling="max"
        )
        self.net.trainable = False
        self.f1 = Dense(1024, activation="relu")
        self.b1 = BatchNormalization()
        self.d1 = Dropout(0.5)
        self.f2 = Dense(21, activation="softmax")

    def call(self, x):
        x = self.net(x)
        x = self.f1(x)
        x = self.b1(x)
        x = self.d1(x)
        y = self.f2(x)
        return y


class MobileNetV2(Model):
    def __init__(self):
        super(MobileNetV2, self).__init__()
        self.net = tf.keras.applications.MobileNetV2(
            input_shape=(224, 224, 3),
            weights=None,
            # weights="./checkpoint/mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.0_224_no_top.h5",
            include_top=False,
            pooling="avg"
        )
        self.net.trainable = False
        self.f1 = Dense(21, activation="softmax")

    def call(self, x):
        x = self.net(x)
        y = self.f1(x)
        return y


class EfficientNetB0(Model):
    def __init__(self):
        super(EfficientNetB0, self).__init__()
        self.net = efn.EfficientNetB0(
            input_shape=(224, 224, 3),
            weights=None,
            # weights="./checkpoint/efficientnet-b0_weights_tf_dim_ordering_tf_kernels_autoaugment_notop.h5",
            include_top=False,
            pooling="avg"
        )
        self.net.trainable = True
        for layers in self.net.layers[:-10]:
            layers.trainable = False
        self.f1 = Dense(21, activation="softmax")

    def call(self, x):
        x = self.net(x)
        y = self.f1(x)
        return y


class EfficientNetB4(Model):
    def __init__(self):
        super(EfficientNetB4, self).__init__()
        self.net = efn.EfficientNetB4(
            input_shape=(224, 224, 3),
            weights=None,
            # weights="./checkpoint/efficientnet-b4_weights_tf_dim_ordering_tf_kernels_autoaugment_notop.h5",
            include_top=False,
            pooling="avg"
        )
        self.net.trainable = True
        for layers in self.net.layers[:-10]:
            layers.trainable = False
        self.f1 = Dense(21, activation="softmax")

    def call(self, x):
        x = self.net(x)
        y = self.f1(x)
        return y


class EfficientNetB7(Model):
    def __init__(self):
        super(EfficientNetB7, self).__init__()
        self.net = efn.EfficientNetB7(
            input_shape=(224, 224, 3),
            weights=None,
            # weights="./checkpoint/efficientnet-b7_weights_tf_dim_ordering_tf_kernels_autoaugment_notop.h5",
            include_top=False,
            pooling="avg"
        )
        self.net.trainable = True
        for layers in self.net.layers[:-10]:
            layers.trainable = False
        self.f1 = Dense(21, activation="softmax")

    def call(self, x):
        x = self.net(x)
        y = self.f1(x)
        return y
