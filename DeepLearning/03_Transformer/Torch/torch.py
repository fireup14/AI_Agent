import torch



# 练习一：观察基础张量
print("练习一：观察基础张量")
x = torch.arange(24).reshape(2, 3, 4)
print(x)
print(x.shape)
print(x[0])
print(x[:, 1, :])
print(x.permute(1, 0, 2).shape)