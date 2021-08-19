
class MagicList():
    def __init__(self, cls_type):
        self.list1 = list(cls_type)


   def set(self, parameter):
       if len(self.list1) == 1:
           raise AssertionError('No Space In list')
       else:
           self.list1.append(parameter)


if __name__ == '__main__':
    m = MagicList(cls_type=float)
    print(m.list1)