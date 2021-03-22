import pickle

f = open("object.dat",'rb')
obj = pickle.load(f)

obj.display()

f.close()