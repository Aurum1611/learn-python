from builtins import staticmethod
class App:
    def __init__(self,name,version):
        self.name=name
        self.version=version
    
    class OS:
        def __init__(self,name):
            self.name=name
        
        @staticmethod
        def disp(v5,V):
            print(v5.name+" runs on "+V.name)

v5=App('WhatsApp','1.23.1')
V=v5.OS('Android')

print('App Name:',v5.name+"\nApp Version:",v5.version)
print('Supported OS:',V.name)
V.disp(v5,V)