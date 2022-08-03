import torch
import numpy as np
import time

#https://pytorch.org/tutorials/beginner/basics/tensor_tutorial.html
#############################初始化张量###################
#值初始化
data = [[1, 2],[3, 4]]
x_data = torch.tensor(data)
print(x_data, '\n')

#值初始化，从numpy数组
np_array = np.array(data, dtype=np.float32) #初始化一个numpy数组，可以指定元素类型
x_np = torch.from_numpy(np_array) #从numpy到tensor，注意tensor与numpy数组将共享内存数据，若不想这样需要进行拷贝操作。
x_np = torch.from_numpy(np_array.copy()) #拷贝源numpy数组，这样改变tensor时不会改变源numpy数组内容
print(x_np, '\n')

#值初始化，从其它的张量
x_ones = torch.ones_like(x_data) # #返回用标量1填充的张量，张量的形状和数据类型与x_data一致
x_ones2 = torch.ones(x_data.size(), dtype=x_data.dtype, layout=x_data.layout, device=x_data.device) #上一个函数的等价形式
print(f"Ones Tensor: \n {x_ones} \n")
print(f"Ones2 Tensor: \n {x_ones2} \n")

#值初始化，从其它的张量
x_rand = torch.rand_like(x_data, dtype=torch.float) # 用[0,1)之间的随机数填充张量, 覆盖x_data的数据类型，形状与x_data一致
x_rand2 = torch.rand(x_data.size(), dtype=torch.float, layout=x_data.layout, device=x_data.device) #上一个函数等价形式
print(f"Random Tensor: \n {x_rand} \n")
print(f"Random Tensor2: \n {x_rand2} \n")


##############内置函数，随机值或固定值初始化#####
shape = (2,3)
rand_tensor = torch.rand(shape, dtype=torch.float) #[0,1)随机数张量，形状为shape， 类型为dtype
ones_tensor = torch.ones(torch.Size(shape)) #全1张量, 用tuple初始化torch.Size对象
zeros_tensor = torch.zeros(torch.Size([2,3])) #全零张量, 用list初始化torch.Size对象
print('\n\n\n','内置函数，随机值或固定值初始化')
print(f"Random Tensor: \n {rand_tensor} \n")
print(f"Ones Tensor: \n {ones_tensor} \n")
print(f"Zeros Tensor: \n {zeros_tensor}")


######################张量属性###################
tensorAtt = torch.rand(3,4) #3×4的张量
print('\n\n\n', '张量属性')
print(f"Shape of tensor: {tensorAtt.shape}")
print(f"Datatype of tensor: {tensorAtt.dtype}")
print(f"Device tensor is stored on: {tensorAtt.device}")


########################张量内置方法###################
#####超过100多种操作，包括基本算术运算、矩阵操作、转置、索引、切片、抽样等#####
####tensor的所有运算都可以在GPU上完成，相比于CPU会有更快的速度####
###注意：需要检查GPU资源是否可用，不要频繁地在CPU和GPU之间交换比较大的张量，因为比较耗时###
##pytorch默认张量在CPU上运行，要转移到GPU上需要显式地声明##
cpu_to_gpu = False

if cpu_to_gpu == True:
    print('\n\n\n', '张量内置方法')
    tensor_cpu = torch.rand(3,4)
    tensor_gpu = tensor_cpu
    #检查GPU是否可用，函数返回值为bool类型
    if torch.cuda.is_available():
        start = time.time()
        tensor_gpu = tensor_cpu.to('cuda') #将cpu的张量放到GPU
        end = time.time()
        print('(3，4)的张量从CPU到GPU耗费的时间为{}s'.format(end-start))

    #CPU和GPU操作时间对比
    tensor_cpu = torch.rand(10000, 10000)
    tensor_gpu = tensor_cpu
    start = time.time()
    tensor_cpu[:,:] = 0.35
    end = time.time()
    print('在CPU中切片的时间为{}s'.format(end-start))
    if torch.cuda.is_available():
        start = time.time()
        tensor_gpu = tensor_cpu.to('cuda') #将cpu的张量放到GPU
        end = time.time()
        print('张量从CPU到GPU耗费的时间为{}s'.format(end-start)) #同一个变量，第二次从CPU到GPU的速度会更快一些
        start = time.time()
        tensor_gpu[:,:] = 0.55
        end = time.time()
        print('在GPU中切片的时间为{}s'.format(end-start))
        

#索引、切片示例
tensor = torch.ones(4, 4)
print('First row: ',tensor[0])
print('First column: ', tensor[:, 0])
print('Last column:', tensor[..., -1])
tensor[:,1] = 0
print(tensor)

#合并张量
t1 = torch.cat([tensor, tensor, tensor], dim=1) #dim=1表示行数不变，在列方向合并，合并后为（4，12）
print(t1)

##算术操作
#计算矩阵相乘
y1 = tensor @ tensor.T #矩阵相乘
y2 = tensor.matmul(tensor.T) #矩阵相乘
y3 = torch.rand_like(tensor) #y3与tensor拥有相同的形状与数据类型
torch.matmul(tensor, tensor.T, out=y3) #将计算结果输出到y3
print('y1 = {}\ny2 = {}\ny3 = {}'.format(y1,y2,y3))

#计算逐元素相乘
z1 = tensor * tensor
z2 = tensor.mul(tensor)
z3 = torch.rand_like(tensor)
torch.mul(tensor, tensor, out=z3)
print('z1 = {}\nz2 = {}\nz3 = {}'.format(z1, z2, z3))

#所有元素求和
agg = tensor.sum() #求矩阵里面所有元素的和
agg_item = agg.item() #取出一个元素的tensor里面的值，作为python内置数据类型
print(agg)
print(agg_item, type(agg_item))

#原地调用，将新值赋给作为输入的变量，以下划线后缀作为标记
#可用节约一定内存，但是在反向传播计算导数时会有一点问题，不建议使用
print(tensor, "\n")
tensor.add_(5)
print(tensor)


#############Tensor到Numpy之间的转换###############

#tensor到numpy
print('tensor to numpy-------------')
t = torch.ones(5)
print(f"t: {t}")
n = t.numpy()
print(f"n: {n}")

#改变tensor时numpy也会变
t.add_(1)
print(f"t: {t}")
print(f"n: {n}")

#numpy到tensor
print('numpy to tensor------------')
n = np.ones(5)
t = torch.from_numpy(n)

#改变numpy数组tensor也会改变，原因是两者共用一块内存
np.add(n, 1, out=n)
print(f"t: {t}")
print(f"n: {n}")