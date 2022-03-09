import efficientnet.tfkeras as efn
import tensorflow as tf
from keras import Model
from keras.layers import Conv2D, Dropout, Dense, BatchNormalization, Activation


class VGG19(Model):
    def __init__(self):
        super(VGG19, self).__init__()
        self.net = tf.keras.applications.VGG19(
            weights="./checkpoint/vgg19_weights_tf_dim_ordering_tf_kernels_notop.h5",
            include_top=False,
            pooling="max"
        )
        self.net.trainable = False
        self.f1 = Dense(1024, activation="relu")
        self.b1 = BatchNormalization()
        self.d1 = Dropout(0.5)
        self.f2 = Dense(20, activation="softmax")

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
            weights="./checkpoint/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5",
            include_top=False,
            pooling="max"
        )
        self.net.trainable = False
        self.f1 = Dense(1024, activation="relu")
        self.b1 = BatchNormalization()
        self.d1 = Dropout(0.5)
        self.f2 = Dense(20, activation="softmax")

    def call(self, x):
        x = self.net(x)
        x = self.f1(x)
        x = self.b1(x)
        x = self.d1(x)
        y = self.f2(x)
        return y


class ResnetBlock(Model):

    def __init__(self, filters, strides=1, residual_path=False):
        super(ResnetBlock, self).__init__()
        self.filters = filters
        self.strides = strides
        self.residual_path = residual_path

        self.c1 = Conv2D(filters, (3, 3), strides=strides, padding='same', use_bias=False)
        self.b1 = BatchNormalization()
        self.a1 = Activation('relu')

        self.c2 = Conv2D(filters, (3, 3), strides=1, padding='same', use_bias=False)
        self.b2 = BatchNormalization()

        # residual_path为True时，对输入进行下采样，即用1x1的卷积核做卷积操作，保证x能和F(x)维度相同，顺利相加
        if residual_path:
            self.down_c1 = Conv2D(filters, (1, 1), strides=strides, padding='same', use_bias=False)
            self.down_b1 = BatchNormalization()

        self.a2 = Activation('relu')

    def call(self, inputs):
        residual = inputs  # residual等于输入值本身，即residual=x
        # 将输入通过卷积、BN层、激活层，计算F(x)
        x = self.c1(inputs)
        x = self.b1(x)
        x = self.a1(x)

        x = self.c2(x)
        y = self.b2(x)

        if self.residual_path:
            residual = self.down_c1(inputs)
            residual = self.down_b1(residual)

        out = self.a2(y + residual)  # 最后输出的是两部分的和，即F(x)+x或F(x)+Wx,再过激活函数
        return out


class ResNet18(Model):

    def __init__(self, block_list, initial_filters=64):  # block_list表示每个block有几个卷积层
        super(ResNet18, self).__init__()
        self.num_blocks = len(block_list)  # 共有几个block
        self.block_list = block_list
        self.out_filters = initial_filters
        self.c1 = Conv2D(self.out_filters, (3, 3), strides=1, padding='same', use_bias=False)
        self.b1 = BatchNormalization()
        self.a1 = Activation('relu')
        self.blocks = tf.keras.models.Sequential()
        # 构建ResNet网络结构
        for block_id in range(len(block_list)):  # 第几个resnet block
            for layer_id in range(block_list[block_id]):  # 第几个卷积层

                if block_id != 0 and layer_id == 0:  # 对除第一个block以外的每个block的输入进行下采样
                    block = ResnetBlock(self.out_filters, strides=2, residual_path=True)
                else:
                    block = ResnetBlock(self.out_filters, residual_path=False)
                self.blocks.add(block)  # 将构建好的block加入resnet
            self.out_filters *= 2  # 下一个block的卷积核数是上一个block的2倍
        self.p1 = tf.keras.layers.GlobalAveragePooling2D()
        self.f1 = tf.keras.layers.Dense(16, activation='softmax', kernel_regularizer=tf.keras.regularizers.l2())

    def call(self, inputs):
        x = self.c1(inputs)
        x = self.b1(x)
        x = self.a1(x)
        x = self.blocks(x)
        x = self.p1(x)
        y = self.f1(x)
        return y


class DenseNet121(Model):
    def __init__(self):
        super(DenseNet121, self).__init__()
        self.net = tf.keras.applications.DenseNet121(
            weights="./checkpoint/densenet121_weights_tf_dim_ordering_tf_kernels_notop.h5",
            include_top=False,
            pooling="max"
        )
        self.net.trainable = False
        self.f1 = Dense(1024, activation="relu")
        self.b1 = BatchNormalization()
        self.d1 = Dropout(0.5)
        self.f2 = Dense(20, activation="softmax")

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
            weights="./checkpoint/mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.0_224_no_top.h5",
            include_top=False,
            pooling="avg"
        )
        self.net.trainable = False
        self.f1 = Dense(20, activation="softmax", kernel_regularizer=tf.keras.regularizers.l2())

    def call(self, x):
        x = self.net(x)
        y = self.f1(x)
        return y


class EfficientNetB0(Model):
    def __init__(self):
        super(EfficientNetB0, self).__init__()
        self.net = efn.EfficientNetB0(
            input_shape=(224, 224, 3),
            weights="./checkpoint/efficientnet-b0_weights_tf_dim_ordering_tf_kernels_autoaugment_notop.h5",
            include_top=False,
            pooling="avg"
        )
        self.net.trainable = True
        for layers in self.net.layers[:-10]:
            layers.trainable = False
        self.f1 = Dense(20, activation="softmax", kernel_regularizer=tf.keras.regularizers.l2())

    def call(self, x):
        x = self.net(x)
        y = self.f1(x)
        return y


class EfficientNetB4(Model):
    def __init__(self):
        super(EfficientNetB4, self).__init__()
        self.net = efn.EfficientNetB4(
            input_shape=(224, 224, 3),
            weights="./checkpoint/efficientnet-b4_weights_tf_dim_ordering_tf_kernels_autoaugment_notop.h5",
            include_top=False,
            pooling="avg"
        )
        self.net.trainable = True
        for layers in self.net.layers[:-10]:
            layers.trainable = False
        self.f1 = Dense(20, activation="softmax", kernel_regularizer=tf.keras.regularizers.l2())

    def call(self, x):
        x = self.net(x)
        y = self.f1(x)
        return y


class EfficientNetB7(Model):
    def __init__(self):
        super(EfficientNetB7, self).__init__()
        self.net = efn.EfficientNetB7(
            input_shape=(224, 224, 3),
            weights="./checkpoint/efficientnet-b7_weights_tf_dim_ordering_tf_kernels_autoaugment_notop.h5",
            include_top=False,
            pooling="avg"
        )
        self.net.trainable = True
        for layers in self.net.layers[:-10]:
            layers.trainable = False
        self.f1 = Dense(20, activation="softmax", kernel_regularizer=tf.keras.regularizers.l2())

    def call(self, x):
        x = self.net(x)
        y = self.f1(x)
        return y
