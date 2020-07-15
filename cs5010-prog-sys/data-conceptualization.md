## Module 1: Data Conceptualization and Intro to Python

#### What is Data?

- Data is _uninterpreted_ information.

- Important to consider the source, quality, scale, and variety of your data.

- Data by itself is useless. Information is data compared to or associated with other things (context, patterns, relationships, etc.). Knowledge is information learned, applied, and understood.

  Data -> Information -> Knowledge -> Decisions

- Data science can enable the creation of data products (ex. Google swine flu tracking).

#### Intro to Python

- Python is a high-level language
- Python is dynamically typed, meaning that you don't have to specify variable data type upon creation.
- Python id(var) function returns the unique identifier of an object, which will remain constant throughout its lifetime. This can be thought of as the address of the object in memory.
- Tuples have most of the same properties as lists, with the key difference that lists are mutable and tuples are immutable.
- Python namespaces are basically variable scopes and contain variables and methods that are defined.
- A sentinel value is a value that carries a special meaning in a program.
- For loops create internal iterators. Can explicitly create an iterator using `iter(item)` where item is a sequence of data (e.g. list or dictionary). Can then proceed through the items in the iterator using `next(iterator)`.
- As far as this course goes, the most important thing when it comes to coding style is consistency. Companies often have their own style guidelines ([PEP 8](https://www.python.org/dev/peps/pep-0008/) is common for Python).

#### Intro to Python, Part 2

- Positional arguments are passed to the function in order, e.g. `function(arg1, arg2)`. Keyword arguments, on the other hand, are passed to the function with specific names, e.g. `function(arg1 = val1, arg2 = val2)`. Python allows you to pass positional arguments and keyword arguments to the same function call, but positional arguments must come first.

- Predicate functions are functions, often used as helper functions, that return true or false.

- Anonymous functions can be created using `lambda x: [transformation of x]`, for example `lambda x: x*x`. This allows you to quickly define a function in-line, without having to previously define it elsewhere.

- Higher-order functions are functions that manipulate functions. Map, filter, and reduce are higher-order functions that are used to apply functions to iterable objects (often lists).

  - Map applies a function to all elements in a sequence. `map(function, my_list)` returns an iterable object of the results of the function applied to each element of the list. `list(map(function, my_list))` returns a list of the results.
  - Filter takes a (usually Boolean) function applies it to all elements, and returns only those that return true when passed to the function. `list(filter(bool_func, my_list))` returns a list of elements in the original list that satisfy the conditions of the Boolean function passed to the filter function. Common use case is filtering out missing data: `list(filter(None, my_list))` removes all values that evaluate to False in Python (including `False, "", None, 0, [], {}, (), 0.0, 0j`).
  - Reduce applies a function on two arguments cumulatively to the items of an iterable object so as to reduce the iterable object to a single value. Need `import functools` to use reduce in Python. For a list $[a_1, a_2, a_n]$ and function $f$, reduce computes $f(f(f(a_1, a_2), a_3)..., a_n)$. In most cases, a for loop is more clear than using the reduce function.

- In object-oriented programming, a class defines a type of object which can have many associated methods. Classes should have an init method for instantiating an instance of the class. Python classes are capitalized by convention, so a class definition and associated init method would look like this:

  ```python
  class MyClass:
  	def __init__(self, param1, param2):
      #the first param of init must always be self
      #self refers to the current instance of the class
      self.param1 = param1
      self.param2 = param2
  ```

  Could then create an instance of this class by calling `MyClass(param1 = val1, param2 = val2)`, which implicitly calls the init method for MyClass.

- Fields are attributes of a class, whereas methods are behaviors of a class.

- Classes' to string method `__str__` defines how objects of that class will be converted to a string. Like the `__init__` method, the to string method is recognized by the compiler. When running `print(classInstance)`, the to string method is implicitly called.

- Derived classes inherit from and extend base classes. This is sometimes called an "is a" relationship, since the derived class object is a base class object (but not vice versa).

  - The first line of the init function for a derived class will call the init function of the base class:

    ```python
    class DerivedClass(BaseClass):
      def __init__(self, baseAttr1, otherAttr1):
        BaseClass.__init__(self, baseAttr1)
        self.otherAttr1 = otherAttr1
    ```

  - Instances of the derived class will have all the attributes and methods available to instances of the base class.