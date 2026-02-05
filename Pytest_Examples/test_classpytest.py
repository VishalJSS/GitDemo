class Testpytest():
    def test_func(self):
        print(type(1))
        return(type(1))
        #assert (type(1)) == int
    
obj=Testpytest()
print(obj.test_func())