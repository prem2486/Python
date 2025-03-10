class A:  
    # Data member  
    var = "Class A Variable"
    
    # Method specific to class A  
    def method1(self):  
        print("Method1 of Class A")  
    
    def method2(self):  
        print("Method2 of Class A")  
    
    # Overridden method  
    def common_method(self):  
        print("Common Method in Class A")  


class B(A):  
    # Data member  
    var = "Class B Variable"
    
    # Method specific to class B  
    def method3(self):  
        print("Method1 of Class B")  
    
    def method4(self):  
        print("Method2 of Class B")  
    
    # Overridden method  
    def common_method(self):  
        print("Common Method in Class B")  



class C(B):  
    # Data member  
    var = "Class C Variable"
    
    # Method specific to class C  
    def method5(self):  
        print("Method1 of Class C")  
    
    def method6(self):  
        print("Method2 of Class C")  
    
    # Overridden method  
    def common_method(self):  
        print("Common Method in Class C")  



if __name__ == "__main__":  
    # Creating Object of Class A  
    objA = A()  
    print("\nClass A Methods:")
    objA.method1()  
    objA.method2()  
    objA.common_method()  
  
    # Creating Object of Class B  
    objB = B()  
    print("\nClass B Methods:")
    objB.method1()  
    objB.method2()  
    objB.method3()  
    objB.method4()  
    objB.common_method()  
  
    # Creating Object of Class C  
    objC = C()  
    print("\nClass C Methods:")
    objC.method1()  
    objC.method2()  
    objC.method3()  
    objC.method4()  
    objC.method5()  
    objC.method6()  
    objC.common_method()  

   
   
    # Runtime Polymorphism using Superclass Reference  
    print("\nOverridden Methods with Super Class Reference:")
    obj = A()
    obj.common_method()
    
    obj = B()
    obj.common_method()
    
    obj = C()
    obj.common_method()

    # Runtime Polymorphism with Data Members  
    print("\nData Members with Super Class Reference:")
    obj = A()
    print("Data Member:", obj.var)
    
    obj = B()
    print("Data Member:", obj.var)
    
    obj = C()
    print("Data Member:", obj.var)
