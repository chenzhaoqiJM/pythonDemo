import paddle
import paddle.nn as nn
import paddle.nn.functional as F
import parl
import numpy as np

#在每一个时间步，模型的输入是一个4维的向量,表示当前小车和杆的状态，模型输出的信号用于控制小车往左或者右移动。
# 当杆没有倒下的时候，每个时间步，环境会给1分的奖励；当杆倒下后，环境不会给任何的奖励，游戏结束。
#Model
#主要定义前向网络，这通常是一个策略网络(Policy Network)或者一个值函数网络(Value Function)，输入是当前环境状态(State)。
class CartpoleModel(parl.Model):
    def __init__(self, obs_dim, act_dim):
        super(CartpoleModel, self).__init__()
        hid1_size = act_dim * 10
        self.fc1 = nn.Linear(obs_dim, hid1_size)
        self.fc2 = nn.Linear(hid1_size, act_dim)

    def forward(self, x):
        out = paddle.tanh(self.fc1(x)) #使用tanh激活函数
        prob = F.softmax(self.fc2(out), axis=-1) #一层FC和softmax激活函数，得到了每个action的概率分布预测。
        return prob
    
#2、Algorithm
#定义了具体的算法来更新前向网络( Model )中的参数，也就是通过定义损失函数以及使用optimizer更新 Model 。
#一个 Algorithm 包含至少一个 Model 。在这个教程中，我们将使用经典的PolicyGradient算法来解决问题。

model = CartpoleModel(act_dim=2) #实例化model
algorithm = parl.algorithms.PolicyGradient(model, lr=1e-3) #model传给对应的更新算法

#Agent
#负责算法与环境的交互，在交互过程中把生成的数据提供给 Algorithm 来更新模型( Model )，也就是数据和算法的交互一般定义在这里。
#我们得要继承 parl.Agent 这个类来实现自己的 Agent ，下面先把 Agent 的代码抛出来，再按照函数解释。
class CartpoleAgent(parl.Agent):
    
    def __init__(self, algorithm):

        super(CartpoleAgent, self).__init__(algorithm)

    def sample(self, obs):

        obs = paddle.to_tensor(obs, dtype='float32')
        prob = self.alg.predict(obs)
        prob = prob.numpy()
        act = np.random.choice(len(prob), 1, p=prob)[0]

        return act

    def predict(self, obs):

        obs = paddle.to_tensor(obs, dtype='float32')
        prob = self.alg.predict(obs)
        act = prob.argmax().numpy()[0]

        return act

    def learn(self, obs, act, reward):

        act = np.expand_dims(act, axis=-1)
        reward = np.expand_dims(reward, axis=-1)
        obs = paddle.to_tensor(obs, dtype='float32')
        act = paddle.to_tensor(act, dtype='int32')
        reward = paddle.to_tensor(reward, dtype='float32')

        loss = self.alg.learn(obs, act, reward)

        return loss.numpy()[0]
#__init__ ：把前面定义好的algorithm传进来，作为agent的一个成员变量，用于后续的数据交互。
# 需要注意的是，这里必须得要初始化父类：super(CartpoleAgent, self).__init__(algorithm) 。

#predict ：根据环境状态返回预测动作（action），一般用于评估和部署agent。
#sample ：根据环境状态返回动作（action），一般用于训练时候采样action进行探索

