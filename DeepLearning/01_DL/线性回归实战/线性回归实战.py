# 定义数据集

# 定义数据特征
x_data  = [1, 2, 3]

# 定义数据标签
y_data = [2, 4, 6]

# 初始化w参数
w = 4

# 定义线性回归的模型
def forword(x):
    return x * w

# 定于损失函数
def cost(xs, ys):
    costvalue = 0
    for x,y in zip(xs, ys):
        y_pred = forword(x)
        costvalue += (y - y_pred)**2
    return costvalue/len(xs)

# 定义计算梯度的函数
def gradient(xs, ys):
    gradvalue = 0
    for x,y in zip(xs, ys):
        gradvalue += 2 * x * (w * x - y)
    return gradvalue/len(xs)


for epoch in range(100):
    # 计算误差损失
    cost_val = cost(x_data, y_data)
    # 计算梯度
    grad_val = gradient(x_data, y_data)
    # 更新参数
    w = w - 0.01 * grad_val
    print(f"训练轮次: {epoch}, 此时的w = {w}, 损失值: {cost_val} ")

print(f"100轮后w已经训练好了，已经可以进行预测和推理，学习时间为四个小时的时候最终的得分为：{forword(4)}")