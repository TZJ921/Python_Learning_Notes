# https://rhettinger.wordpress.com/2011/05/26/super-considered-super/

# 一个简单的例子
# 作用是简单的继承了一下dict，在更新dict时，打印更新的值
class LoggingDict(dict):
    def __setitem__(self, key, value):
        print(key, value)
        super().__setitem__(key, value)

# 使用super的好处是，不需要硬编码类的名字，就可以直接改变继承，比如
# 如果不用super，我们需要写成：dict.__setitem__(self, key, value)
class LoggingDict(SomeOtherMapping):
    def __setitem__(self, key, value):
        print(key, value)
        super().__setitem__(key, value)

# 创建一个可以打印key，value的OrderDict
import collections
class LoggingOD(LoggingDict, collections.OrderedDict):
    pass

# 打印祖先树的顺序
# 结果为LoggingOD -> LoggingDict -> OrderDict -> dict -> object
# 所以在调用__setitem__时，一级一级的向上寻找，而LoggingDict的super()是OrderDict
print(LoggingOD.__mro__)

# 针对不定参数
class Shape:
    def __init__(self, shapename, **kwds):
        self.shapename = shapename
        super().__init__(**kwds)

class ColoredShape(Shape):
    def __init__(self, color, **kwds):
        self.color = color
        super().__init__(**kwds)

cs = ColoredShape(color='red', shapename='circle')


# 怎样确保目标方法存在呢？
# 可以使用防御式编程defensive programming
# 例如draw这个方法可能调用链上没有，为防止报错，编写一个Root.draw
class Root:
    def draw(self):
        # the delegation chain stops here
        # 确保super没有draw方法，如果有，抛出异常
        assert not hasattr(super(), 'draw')

class Shape(Root):
    def __init__(self, shapename, **kwds):
        self.shapename = shapename
        super().__init__(**kwds)
    def draw(self):
        print('Drawing. Setting shape to:', self.shapename)
        super().draw()


class ColoredShape(Shape):
    def __init__(self, color, **kwds):
        self.color = color
        super().__init__(**kwds)
    def draw(self):
        print('Drawing. Setting color to:', self.color)
        super().draw()

cs = ColoredShape(color='blue', shapename='square')
cs.draw()

# mro -> method resolution order
# 需要在调用链上的每一个method里面写super

# 将一个第三方类改写成可以放在调用链里的
class Moveable:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        print('Drawing at position:', self.x, self.y)

class MoveableAdapter(Root):
    def __init__(self, x, y, **kwds):
        self.moveable = Moveable(x, y)
        super().__init__(**kwds)
    def draw(self):
        self.moveable.draw()
        super().draw()

class MoveableColoredShape(ColoredShape, MoveableAdapter):
    pass

MoveableColoredShape(color='red', shapename='triangle', x=10, y=20).draw()


from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    'Counter that remembers the order elements are first seen'
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))
    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)

oc = OrderedCounter('abracadabra')
