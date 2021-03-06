## Module 6: Software Engineering

- Software engineering involves building large systems and modifying them over time in a disciplined, scientific way.
- Software engineering is both a technical and managerial discipline, as it involves completing projects on time and in budget.
- "Programming in the small" is very different from "programming in the large" (analogy of crossing a creek vs. crossing Strait of Gibraltar). Differences in maintenance, cost, risk, etc.
- Software development lifecycle involves requirements (specs from client on what system should do), design (creation of a blueprint for how a solution will be implemented), implementation (coding), integration (combining parts of the system and ensuring they work together in the environment), and maintenance (fixing errors, adding enhancements, and adapting to work in changing environments).
  - Maintenance is generally the largest phase.
  - Most difficult part of requirements is figuring out what they are from the client.
- Two types of requirements: functional and non-functional. Functional requirements describe what the system should do, but not how it should do it. Non-functional requirements describe how something is done, and add qualities and/or constraints to a functional requirement.
  - Non-functional requirements must be objective rather than subjective, else they can't be tested.
  - Non-functional requirements are qualities and often involve accessibility, privacy, efficiency, scalability, etc. Non-functional requirements add detail to functional requirements (can have a functional requirement with no associated non-functional requirements, but not vice versa).
  - Constraints are client-expressed design requests that are often implementation-specific. Constraints are related to design rather than requirements and speak to "how" rather than "what" of the solution. Examples: must be written in Python, must use NetBadge security for login.
- Requirements are not expressed in terms of a solution.
- Want to find errors as early as possible, as they become more expensive when they are found later in the lifecycle.
  - "Do better early" principle.
- When coding, you should alternate between coding and testing, quickly testing each small addition to your code as you go. Don't code something that depends on other things that haven't been tested.

#### Class Discussion: Functional vs. Non-Functional Requirements

Are each of the following functional or non-functional requirements, or not requirement statements at all?

- The reloading of the user statistics  performs 90% of the time below 100 ms. when tested on machines with the  performances specified in appendix G part 2 and the load below 10% for  the CPU, below 50% for memory and no active R/W disk operations. **Non-functional**
- The application is written in C#. **Ambiguous** - could be a requirement if it's a client ask, but could be part of design if it is the wish of the lead developer
- The main window of the application  has a blue (#00f) 10px border with pink (#fcc) filled circles, those  circles being placed at the inner edge of the border and being 3px in  diameter, separated by 20px from each other. **Non-functional** because it's a testable property of the product, but not what the product is intended to do
- The vehicle tracking system measures the speed with a precision of ±0.016 mph. **Non-functional**
- The vehicle tracking system measures the speed of the vehicle. **Functional**
- The pages of the website take 850 ms. to load. **Not a requirement** because it's dependent on hardware (how would this be tested?)