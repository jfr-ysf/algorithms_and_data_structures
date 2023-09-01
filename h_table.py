class Hash_table:
    def __init__(self):
        self.v = [0] * 127
        self.s = 127
    def hash(self, x):
        return self.s % x
    def insert(self, x):
        if self.v[self.hash(x)] == 0:
            self.v[self.hash(x)] = x
        else:
            self.v[self.hash(x)] = [x, self.v[self.hash(x)]]
    def search(self, x):
        '''
        Example:
            A.search_index(14) //returns: some_index or Object is not found
            Function for searching by value.
            Returns index if value is in array and None if it's not
        '''
        if self.v[self.hash(x)] == x:
            return self.hash(x)
        elif type(self.v[self.hash(x)])==list:
            for i in range(len(self.v[self.hash(x)])):
                if self.v[self.hash(x)][i] == x:
                    return self.hash(x), i
        else:
            return None
class Hthih:
    '''
    HTHIH - Hash_table_hash_in_hash
    '''
    def __init__(self):
        self.v = [0] * 127
        self.s = 127
	def hash(self, x):
        return self.s % x
    def hash1(self, x):
        global a
        global b
        a = 31415
        b = 27183
        a = (a * b) % (b//37)
        return (a * x) % 37
    def ihih(self, x):
        """
        IHIH - Insert_hash_in_hash
        """
        if self.v[self.hash(x)] == 0:
            self.v[self.hash(x)] = x
        elif type(self.v[self.hash(x)]) == list:
            for i in range(len(self.v[self.hash(x)])):
                if i == self.hash1(x):
                    self.v[self.hash(x)] = [x, self.v[self.hash(x)]]
                    break
        else:
            tmp = self.v[self.hash(x)]
            self.v[self.hash(x)] = [0] * 37
            self.v[self.hash(x)][self.hash1(x)] = x
            self.v[self.hash(x)][self.hash1(tmp)] = tmp
    def shih(self, x):
        '''
        Example:
            A.search_index(14) //returns: some_index or Object is not found
            Function for searching by value.
            Returns index if value is in array and None if it's not
        '''
        if self.v[self.hash(x)] == x:
            return self.hash(x)
        if self.v[self.hash(x)][self.hash1(x)] == x:
            return self.hash(x), self.hash1(x)
        return None
#Test OF Hash_table()
a = Hash_table()
b = int(input("Enter value_1: "))
c = int(input("Enter value_2: "))
print(a.s)
a.insert(b)
a.insert(c)
print('a.hash(b)', a.hash(b))
print('a.hash(c)', a.hash(c))
print("a.search(b)", a.search(b))
print("a.search(c)", a.search(c))
print("a.v[hash(b)] - ", a.v[a.hash(b)])
print("a.v[hash(c)] - ", a.v[a.hash(c)])
#Test OF Hthih()
a1 = Hthih()
b1 = int(input("Enter value_1_1: "))
c1 = int(input("Enter value_1_2: "))
print(a1.s)
a1.ihih(b1)
a1.ihih(c1)
print('a1.hash(b1)', a1.hash(b1))
print('a1.hash(c1)', a1.hash(c1))
print("a1.shih(b1)", a1.shih(b1))
print("a1.shih(c1)", a1.shih(c1))
print("a1.v[a1.hash(b1)] - ", a1.v[a1.hash(b1)])
print("a1.v[a1.hash(c1)] - ", a1.v[a1.hash(c1)])
input()
/