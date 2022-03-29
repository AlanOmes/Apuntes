class A:

    def mostrar_a(self):
        print('A')
    
class B:

    def mostrar_b(self):
        print('B')

class C(A, B):
    def mostrar_c(self):
        print('C')

c = C()

c.mostrar_a()
c.mostrar_b()
c.mostrar_c()
