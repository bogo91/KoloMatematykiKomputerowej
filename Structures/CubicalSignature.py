#from copy import deepcopy

class CubicalSignature:

    def __init__(self, sig):
        self.sig = sig
    def get_len(self):
        return len(self.sig)
    def get_dim(self):
        return sum(len(x) for x in self.sig) - len(self.sig)
    def get_faces(self):
        return [CubicalSignature(self.sig[:i]+[[self.sig[i][0]]]+self.sig[i+1:]) for i in range(len(self.sig)) if len(self.sig[i])>1] + [CubicalSignature(self.sig[:i]+[[self.sig[i][1]]]+self.sig[i+1:]) for i in range(len(self.sig)) if len(self.sig[i])>1]
    def __str__(self):
        return str(self.sig)
    def __hash__(self):
        return hash(str(self.sig))
    def __eq__(self,other):
        return str(self)==str(other)
