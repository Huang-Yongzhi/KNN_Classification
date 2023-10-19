# 原始文件大小太大了，大于上限100M，要切分成两部分
def split_integer_file(file_path):
    # 读取整个文件
    with open(file_path, "r") as file:
        content = file.readlines()

    # 将整数数据分成两部分
    total_numbers = len(content)
    half_numbers = total_numbers // 2

    first_half = content[:half_numbers]
    second_half = content[half_numbers:]

    # 将分割后的数据写入两个不同的文件
    with open("mnist_x_1", "w") as file:
        file.writelines(first_half)

    with open("mnist_x_2", "w") as file:
        file.writelines(second_half)

# 调用函数并传递文件路径
split_integer_file(".\mnist_x")