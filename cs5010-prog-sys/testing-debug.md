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

