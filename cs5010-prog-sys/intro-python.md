### Module 1: Data Conceptualization and Intro to Python

#### What is Data?

- Data is _uninterpreted_ information.

- Important to consider the source, quality, scale, and variety of your data.

- Data by itself is useless. Information is data compared to or associated with other things (context, patterns, relationships, etc.). Knowledge is information learned, applied, and understood.

  Data -> Information -> Knowledge -> Decisions

- Data science can enable the creation of data products (ex. Google swine flu tracking).

#### Intro to Python

- Python is a high-level language
- Python is dynamically typed, meaning that you don't have to specify variable data type upon creation. It is also strongly typed, meaning that, for example, you can't add an integer and a string.
- Python id(var) function returns the unique identifier of an object, which will remain constant throughout its lifetime. This can be thought of as the address of the object in memory.
- Tuples have most of the same properties as lists, with the key difference that lists are mutable and tuples are immutable.
- Python namespaces are basically variable scopes and contain variables and methods that are defined.
- A sentinel value is a value that carries a special meaning in a program.
- For loops create internal iterators. Can explicitly create an iterator using `iter(item)` where item is a sequence of data (e.g. list or dictionary). Can then proceed through the items in the iterator using `next(iterator)`.
- As far as this course goes, the most important thing when it comes to coding style is consistency. Companies often have their own style guidelines ([PEP 8](https://www.python.org/dev/peps/pep-0008/) is common for Python).

### Module 2: Intro to Python, Part II

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

- Why do we use classes? Encapsulation and abstraction make code more efficient, readable, reproducible, and easier to debug.

- Classes are like blueprints, and instances of the class are like buildings.

- Classes' to string method `__str__` defines how objects of that class will be converted to a string. Like the `__init__` method, the to string method is recognized by the compiler. When running `print(classInstance)`, the to string method is implicitly called.

- Derived classes inherit from and extend base classes. This is sometimes called an "is a" relationship, since the derived class object is a base class object (but not vice versa).

  - The first line of the init function for a derived class needs to call the init function of the base class:

    ```python
    class DerivedClass(BaseClass):
      def __init__(self, baseAttr1, otherAttr1):
        BaseClass.__init__(self, baseAttr1)
        self.otherAttr1 = otherAttr1
    ```

  - Instances of the derived class will have all the attributes and methods available to instances of the base class.

  - There can be many levels of subclasses (sub-subclasses, etc.). For a sub-subclass, you only need to call the init method of its parent (the subclass), not the parent and grandparent.

### Module 3: Intro to Python, Part III

- All class fields and methods are public by default in Python. Conventionally, protected fields and methods (accessible only from within the class and its subclasses) are designated by single underscore prefix. Private fields and methods (not able to access from outside the class) are designated by a prefix of two underscores.

  - Protected fields/methods are accessible outside the class but shouldn't be. Private fields/methods cannot be accessed outside the class and will throw an error.

- Every class instance has a built-in attribute `__class__` which is the object's class.

- Python class attributes are public and can be accessed and updated using the dot operator. `instance.attribute` returns the attribute value for that particular instance, and `instance.attribute = new_val` sets the attribute to a new value for that instance.

- Objects have a destructor method `object.__del__(self)` that is called when the instance is about to be destroyed.

- When default values are passes to a function definition, they are created at the time the def statement is executed (when the function is created), not each time the function is called. When mutable objects (lists, dictionaries, etc.) are supplied as default arguments and then mutated, the mutated object will be passed in future function calls. To avoid issues arising from this, you must be sure a new object is created each time the function is called, like so:

  ```python
  def my_function(element, aList = None):
    if aList is None:
      aList = []
      #do somethine with aList
      #return something
  ```

  Using `def my_function(element, aList = [])` should not be used, as aList may no longer be equal to an empty list every time the function is called.

- Base class methods can be overwritten by derived class methods with the same name. Because of something called runtime polymorphism, the compiler will first look for a called method in the derived class, run it if it is found, and look for that method in the base class only if it is not found in the derived class. This is useful when you want the derived class to exhibit the same functionality as the base but with more specific functionality.

- Compilation (syntax) errors are caught upon compilation of the program and are often typographical errors, like mispelling a function or missing a parenthesis. Runtime errors, on the other hand, occur after compilation and during running of the program, such as divide by zero or file not found errors.

  - When Python encounters runtime errors, it raises an Exception, an object containing a description of the error and the traceback.

- If you are aware of what exceptions might be thrown by your code, you can handle them with try-except statements.

  ```python
  try:
    #some code
  except:
    #code to run when try code raises an exception
  except FileNotFoundError as err:
    #can optionally specify multiple except statements for different types of exceptions
    #do something with err, like print or log
    raise #optional
  else:
    #runs if try block succeeds
  finally: #optional
    #code to run always after try/except statements regardless of whether exceptions were raised
  ```

  Python has an exception [hierarchy](https://docs.python.org/3/library/exceptions.html#exception-hierarchy), so if you want one except statement for a subclass exception and another except statement for its parent class exception, you must put the subclass except statement first.

- Further [reading](https://jakevdp.github.io/PythonDataScienceHandbook/01.06-errors-and-debugging.html) on jupyter notebook error handling and debugging.

- TypeErrors occur when an operation or function is applied to an object of inappropriate type (e.g. int instead of list). ValueErrors occur when an operation or function receives an object that has the right type but an inappropriate value (e.g. an out of bounds error such as a negative integer when only positive integers are allowed).