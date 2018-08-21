class Root(object):
    def __init__(self):
        print('ok, good luck!')
        
class A(Root):
    def __init__(self):
        super(A, self).__init__()
 
class B(A):
    def __init__(self):
        super(B, self).__init__()
        
class C(B):
    def __init__(self, wo):
        self.x = wo
        super(C, self).__init__()

c=C(5)
print(C.mro())