import os
import pickle

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from PIL import Image, ImageQt
from PySide6.QtGui import QPixmap

plt.rcParams['font.sans-serif'] = ["SimHei"]
plt.rcParams['axes.unicode_minus'] = False


def show(history, model_name):
    figure_save_path = "./checkpoint/flower_" + model_name + ".png"
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['font.family'] = ['Times New Roman']
    plt.rcParams['axes.unicode_minus'] = False

    acc = history['sparse_categorical_accuracy']
    val_acc = history['val_sparse_categorical_accuracy']
    loss = history['loss']
    val_loss = history['val_loss']
    # print(history)
    # 测试集结果
    x = list(history["loss_test"].keys())
    loss_test = list(history["loss_test"].values())
    acc_test = list(history["acc_test"].values())
    print("lost_test", loss_test)
    print("acc_test", acc_test)
    epochs = len(history['loss'])

    # 作图：训练集和验证集准确率曲线图，测试集最终结果点
    plt.figure(figsize=(12, 4))  # 画布大小12×3英寸
    plt.subplot(1, 2, 1)  # 子图1用于记录准确率
    plt.plot(np.arange(1, epochs + 1), acc, label='train accuracy')  # 绘制训练集准确率
    plt.plot(np.arange(1, epochs + 1), val_acc, label='validation accuracy')  # 绘制验证集准确率
    plt.scatter(x, acc_test, marker="o", color="red")  # 绘制测试集准确率散点
    # for i, x_i in enumerate(x):
    #     plt.plot([x_i, x_i], [0, acc_test[i]], linestyle="--")
    #     plt.plot([0, x_i], [acc_test[i], acc_test[i]], linestyle="--")
    for i, x_i in enumerate(x):  # 循环为测试集散点注解
        plt.annotate("acc=%.3f " % acc_test[i],  # 注解文字
                     xytext=(-40, -30),  # 注解文字偏移
                     xycoords="data",
                     xy=(x_i, acc_test[i]),  # 注解坐标
                     textcoords='offset points',  # 注解方式
                     arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))  # 注解箭头
    plt.xlabel("epochs")  # x轴标签
    plt.title('classification accuracy')  # y轴标签
    plt.legend()  # 显示图注

    plt.subplot(1, 2, 2)  # 子图2用于记录损失函数值
    plt.plot(np.arange(1, epochs + 1), loss, label='train loss')  # 绘制训练集损失函数值
    plt.plot(np.arange(1, epochs + 1), val_loss, label='validation loss')  # 绘制验证集损失函数之
    plt.scatter(x, loss_test, marker="o", color="red")  # 绘制测试集损失函数值散点
    for i, x_i in enumerate(x):  # 循环为测试集散点注解
        plt.annotate("loss=%.3f " % loss_test[i],
                     xytext=(-50, 20),
                     xycoords="data",
                     xy=(x_i, loss_test[i]),
                     textcoords='offset points',
                     arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
    plt.xlabel("epochs")
    plt.title('loss function value')
    plt.legend()

    plt.savefig(figure_save_path)  # 存储图像
    plt.show()  # 显示图像


def history_show(model_name):
    history_save_path = "./checkpoint/flower_" + model_name + "_history.pickle"
    history = {"sparse_categorical_accuracy": [],
               "val_sparse_categorical_accuracy": [],
               "loss": [],
               "val_loss": [],
               "loss_test": {},
               "acc_test": {},
               "batch_size": [],
               "lr": []
               }
    count = []
    if os.path.exists(history_save_path):
        with open(history_save_path, 'rb') as file:
            all_epochs = 0  # 记录历史轮次
            while True:
                # pickle.dump()以mode="ab"模式下追加的为多个不同的pickle对象
                # 因此需要多次dump将其多个对象加载出来
                try:
                    history_load = pickle.load(file)  # 加载多次的历史记录
                    # 本记录若干轮次训练集和验证集acc,loss的追加
                    history["sparse_categorical_accuracy"].extend(history_load["sparse_categorical_accuracy"])
                    history["val_sparse_categorical_accuracy"].extend(history_load["val_sparse_categorical_accuracy"])
                    history["loss"].extend(history_load["loss"])
                    history["val_loss"].extend(history_load["val_loss"])
                    this_epoch = len(history_load["loss"])  # 记录本记录的轮次
                    count.append(this_epoch)
                    all_epochs += this_epoch
                    # 本记录测试集acc,loss的键值对的追加
                    history["loss_test"][all_epochs] = history_load["loss_test"]
                    history["acc_test"][all_epochs] = history_load["acc_test"]
                    # 本记录批量大小和学习率的追加
                    history["batch_size"].append(history_load["batch_size"])
                    history["lr"].append(history_load["lr"])
                except EOFError:
                    train_count = len(count)
                    print("总共进行" + str(train_count) + "次训练：")
                    for i in range(train_count):
                        print("""第{}次训练：\n\
                                 \t训练轮数为：{}轮\n\
                                 \t批量大小为：{}张图片\n\
                                 \t学习率为：{:g}\n
                              """.format(i + 1, count[i], history["batch_size"][i], history["lr"][i]))
                    print("总共训练轮数：%d轮\n" % all_epochs)
                    break
    show(history, model_name)


def load_model(model):
    # 对传入的模型的历史数据作图，并且进行预测
    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
                  metrics=['sparse_categorical_accuracy'])

    model_name = model.__class__.__name__
    checkpoint_save_path = "./checkpoint/flower_" + model_name + ".ckpt"
    if os.path.exists(checkpoint_save_path + '.index'):
        print('-------------load the model-----------------')
        model.load_weights(checkpoint_save_path)
        return True
    else:
        print("No model is chosen")
        return False


def model_predict(model, pixmap: QPixmap):
    flowers = ["bougainvillea", "daisy", "dandelion", "gardenia", "hibiscus", "hydrangea",
               "iris", "lily", "lotus", "morningglory", "peachflower", "peony", "phalaenopsis",
               "rose", "sunflower", "tulip"]
    img = ImageQt.fromqpixmap(pixmap)  # QPixmap -> Image
    # img = Image.open(image_path)
    img = img.convert("RGB")
    img = img.resize((224, 224), Image.ANTIALIAS)
    img_arr = np.array(img)
    img_arr = img_arr / 255.0
    x = np.reshape(img_arr, (1, 224, 224, 3))
    result = model.predict(x)
    index = int(tf.argmax(result, axis=1).numpy())
    return list(result.flatten()), flowers[index], index
