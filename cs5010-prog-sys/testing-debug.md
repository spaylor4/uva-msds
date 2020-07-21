### Module 5: Software Testing and Debugging

#### Testing & Verification

- “Program testing can effectively show the presence of bugs but is hopeless for showing their absence.” -Edsger Dijkstra
- Formal verification involves proof, which is complex and difficult. Empirical testing involves showing that code works on several inputs, and it is much easier than proof (though harder than writing code).
  - Unit testing: test the smallest possible units of the spec for each flow path.
  - Integration testing: test that units work together.
  - Beta testing (accecptance testing): give product to real users to try out.
- Two types of unit testing:
  - Black box testing is based on specifications and only looks at inputs and outputs, not the code itself.
  - White box testing is based on the logic of the code and examines the different flow paths.

#### Test-Driven Development (TDD) & Unit Testing

- In TDD, developers write their own unit tests for each method as they write the method itself.
  - Encourages modularization of code. Allows you to build on existing code knowing that what's written is correct (avoids a "house of cards").
  - Generally will have several unit tests per method to test their functionality. If your test can fail in more than one way, make a separate test for each way.
  - Good practice to write test "stubs" (just a signature and dummy return value) based on the specifications before writing the code. This will help you think about every part of the specs and avoid testing only what works.
- Often use Python's assert methods (`assertEquals(a, b)`, `assertTrue(x)`, `assertIn(a, b)`, etc.) to check that the method did what you expected. These are in the `unittest.TestCase` class (need to `import unittest`).
  - Generally create a class for testing one particular method. This class will inherit from `unittest.TestCase`.
- Tools can give your test coverage: the % of lines covered, % of flows covered (often 0 when there are infinite options), and % of input sequences covered (also often 0).
- In designing unit tests, it's important to consider the input space (arguments, inputs, and events), output space (returns, output streams, and side effects), and internal space (input/output spaces of operations within the method).
  - You will often have an infinite number of input options, so you'll never be able to test every one. Instead, you can divide them into equivalence classes of sets that will behave the same way. Then you can test boundary values, values in the middle of the equivalence classes, and unique/corner cases.
- When writing unit tests in Python, you should:
  - Include the word "test" in the filename.
  - `import unittest` at the top of the file.
  - Import the method you are testing from its script.
  - Create a class that inherits from unittest.TestCase.
  - Create a function named "test_[descrip_of_test]" and write code within it as you would normally use the method in question. Then use assert statements to check that the expected value and actual value are the same.
- Don't write unit tests that you expect to fail. Instead use `assertFalse` or another appropriate assert statement. 