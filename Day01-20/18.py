# import time


# # 定义时钟类
# class Clock:
#     """数字时钟"""

#     def __init__(self, hour=0, minute=0, second=0):
#         """初始化方法
#         :param hour: 时
#         :param minute: 分
#         :param second: 秒
#         """
#         self.hour = hour
#         self.min = minute
#         self.sec = second

#     def run(self):
#         """走字"""
#         self.sec += 1
#         if self.sec == 60:
#             self.sec = 0
#             self.min += 1
#             if self.min == 60:
#                 self.min = 0
#                 self.hour += 1
#                 if self.hour == 24:
#                     self.hour = 0

#     def show(self):
#         """显示时间"""
#         return f'{self.hour:0>2d}:{self.min:0>2d}:{self.sec:0>2d}'


# # 创建时钟对象
# clock = Clock(23, 59, 58)
# while True:
#     # 给时钟对象发消息读取时间
#     print(clock.show())
#     # 休眠1秒钟
#     time.sleep(1)
#     # 给时钟对象发消息使其走字
#     clock.run()


class Point:
    """平面上的点"""

    def __init__(self, x=0, y=0):
        """初始化方法
        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x, self.y = x, y

    def distance_to(self, other):
        """计算与另一个点的距离
        :param other: 另一个点
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx * dx + dy * dy) ** 0.5

    def __str__(self):
        return f'({self.x}, {self.y})'


p1 = Point(3, 5)
p2 = Point(6, 9)
print(dir(p1))
print(p1)  # 调用对象的__str__魔法方法
print(p2)
print(p1.distance_to(p2))