import torch
from torchvision.datasets import FashionMNIST
from torchvision import transforms
import torch.utils.data as Data
import numpy as np
import matplotlib.pyplot as plt
from model import LeNet
import torch.nn as nn
import pandas as pd


def test_data_process():
    test_data = FashionMNIST(root='./data',
                              train=False,
                              transform=transforms.Compose([transforms.Resize(size=28), transforms.ToTensor()]),
                              download=True)


    test_dataloader = Data.DataLoader(dataset=test_data,
                                       batch_size=1,
                                       shuffle=True,
                                       num_workers=0)

    return test_dataloader


def test_model_process(model, test_dataloader):

    # 设定训练所用到的设备，有GPU用GPU没有GPU用CPU
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # 将模型放到设备中
    model.to(device)
    # 初始化参数
    test_accuracy = 0.0
    test_num = 0
    # 在推理过程中不需要反向传播
    with torch.no_grad():
        # 对每一个mini-batch计算
        for test_data_x, test_data_y in test_dataloader:
            # 将特征放入到验证设备中
            test_data_x = test_data_x.to(device)
            # 将标签放入到验证设备中
            test_data_y = test_data_y.to(device)
            # 设置模型为评估模式
            model.eval()
            # 前向传播过程，输入为一个batch，输出为一个batch中对应的预测
            output = model(test_data_x)
            # 查找每一行中最大值对应的行标
            pre_lab = torch.argmax(output, dim=1)
            # 如果预测正确，则准确度 test_accuracy 加1
            test_accuracy += torch.sum(pre_lab == test_data_y.data)
            # 当前用于验证的样本数量
            test_num += test_data_x.size(0)

    test_acc_rate = test_accuracy.double().item() / test_num
    print("测试准确率： ",test_acc_rate)





if __name__=="__main__":
    # 加载模型
    model = LeNet()
    model.load_state_dict(torch.load('best_model.pth'))
    # 加载测试数据
    test_dataloader = test_data_process()
    # 加载模型测试的函数
    test_model_process(model, test_dataloader)



