class MyClass:
    class_var = 0
    
    @classmethod
    def class_method(cls):
        return cls.class_var
    
    @staticmethod
    def static_method():
        return f"This is a static method {MyClass.class_var}."

print(MyClass.class_method())  # Output: 0
print(MyClass.static_method())  # Output: This is a static method.