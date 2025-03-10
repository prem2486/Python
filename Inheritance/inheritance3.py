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
