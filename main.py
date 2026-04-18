# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


import torch
import torch.nn as nn
from torch import optim
from torch.utils.data import TensorDataset, DataLoader


# 定义模型
class MyClassifier(nn.Module):#day0分类模型
    def __init__(self, input_size, hidden_size, num_classes):
        super().__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        return x

    def fit(model, X_train, y_train, X_val=None, y_val=None,
            epochs=100, batch_size=32, lr=0.001, verbose=True):
        """
        模拟sklearn的fit()方法
        """
        # 转tensor
        X_train = torch.FloatTensor(X_train)
        y_train = torch.LongTensor(y_train)

        # 数据加载器
        train_dataset = TensorDataset(X_train, y_train)
        train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

        # 损失函数和优化器
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.Adam(model.parameters(), lr=lr)

        # 训练循环
        for epoch in range(epochs):
            model.train()  # 训练模式
        total_loss = 0
        correct = 0
        total = 0

        for batch_X, batch_y in train_loader:
            # 前向传播
            outputs = model(batch_X)
            loss = criterion(outputs, batch_y)

            # 反向传播
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            # 统计
            total_loss += loss.item()
            _, predicted = torch.max(outputs.data, 1)
            total += batch_y.size(0)
            correct += (predicted == batch_y).sum().item()

        # 打印
        if verbose and (epoch + 1) % 10 == 0:
            acc = correct / total
            print(f'Epoch [{epoch+1}/{epochs}], Loss: {total_loss:.4f}, Acc: {acc:.4f}')
        return model


# 使用
def use0():
    model = MyClassifier(input_size=768, hidden_size=256, num_classes=10)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)



# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    use0()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
