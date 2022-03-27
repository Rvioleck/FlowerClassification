import efficientnet.keras as efn
from tensorflow import keras
from tensorflow.python.keras import Model
from tensorflow.python.keras.layers import Dense


class VGG19(Model):
    def __init__(self):
        super(VGG19, self).__init__()
        self.net = keras.applications.VGG19(
            weights=None,
            include_top=False,
            pooling="max"
        )
        self.f = Dense(24, activation="softmax")

    def call(self, x, **kwargs):
        x = self.net(x)
        y = self.f(x)
        return y


class InceptionV3(Model):
    def __init__(self):
        super(InceptionV3, self).__init__()
        self.net = keras.applications.InceptionV3(
            weights=None,
            include_top=False,
            pooling="max"
        )
        self.f = Dense(24, activation="softmax")

    def call(self, x, **kwargs):
        x = self.net(x)
        y = self.f(x)
        return y


class DenseNet121(Model):
    def __init__(self):
        super(DenseNet121, self).__init__()
        self.net = keras.applications.DenseNet121(
            weights=None,
            include_top=False,
            pooling="max"
        )
        self.f = Dense(24, activation="softmax")

    def call(self, x, **kwargs):
        x = self.net(x)
        y = self.f(x)
        return y


class MobileNetV2(Model):
    def __init__(self):
        super(MobileNetV2, self).__init__()
        self.net = keras.applications.MobileNetV2(
            input_shape=(224, 224, 3),
            weights=None,
            include_top=False,
            pooling="avg"
        )
        self.f = Dense(24, activation="softmax")

    def call(self, x, **kwargs):
        x = self.net(x)
        y = self.f(x)
        return y


class EfficientNetB0(Model):
    def __init__(self):
        super(EfficientNetB0, self).__init__()
        self.net = efn.EfficientNetB0(
            input_shape=(224, 224, 3),
            weights=None,
            include_top=False,
            pooling="avg"
        )
        self.f = Dense(24, activation="softmax")

    def call(self, x, **kwargs):
        x = self.net(x)
        y = self.f(x)
        return y


class EfficientNetB1(Model):
    def __init__(self):
        super(EfficientNetB1, self).__init__()
        self.net = efn.EfficientNetB1(
            input_shape=(224, 224, 3),
            weights=None,
            include_top=False,
            pooling="avg"
        )
        self.f = Dense(24, activation="softmax")

    def call(self, x, **kwargs):
        x = self.net(x)
        y = self.f(x)
        return y


class EfficientNetB2(Model):
    def __init__(self):
        super(EfficientNetB2, self).__init__()
        self.net = efn.EfficientNetB2(
            input_shape=(224, 224, 3),
            weights=None,
            include_top=False,
            pooling="avg"
        )
        self.f = Dense(24, activation="softmax")

    def call(self, x, **kwargs):
        x = self.net(x)
        y = self.f(x)
        return y


class EfficientNetB3(Model):
    def __init__(self):
        super(EfficientNetB3, self).__init__()
        self.net = efn.EfficientNetB3(
            input_shape=(224, 224, 3),
            weights=None,
            include_top=False,
            pooling="avg"
        )
        self.f = Dense(24, activation="softmax")

    def call(self, x, **kwargs):
        x = self.net(x)
        y = self.f(x)
        return y


class EfficientNetB4(Model):
    def __init__(self):
        super(EfficientNetB4, self).__init__()
        self.net = efn.EfficientNetB4(
            input_shape=(224, 224, 3),
            weights=None,
            include_top=False,
            pooling="avg"
        )
        self.f = Dense(24, activation="softmax")

    def call(self, x, **kwargs):
        x = self.net(x)
        y = self.f(x)
        return y


class EfficientNetB7(Model):
    def __init__(self):
        super(EfficientNetB7, self).__init__()
        self.net = efn.EfficientNetB7(
            input_shape=(224, 224, 3),
            weights=None,
            include_top=False,
            pooling="avg"
        )
        self.f = Dense(24, activation="softmax")

    def call(self, x, **kwargs):
        x = self.net(x)
        y = self.f(x)
        return y
