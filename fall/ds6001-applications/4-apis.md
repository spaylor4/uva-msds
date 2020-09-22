# Module 4: Working with APIs in Python

Readings: [Python API Develpment Fundamentals](https://learning.oreilly.com/library/view/python-api-development/9781838983994/) ch. 3; [Objects of Intense Feeling](http://computationalculture.net/objects-of-intense-feeling-the-case-of-the-twitter-api/)

- API stands for application programming interface, and it helps a website/app communicate with the backend. Analogous to a waiter acting as an intermediary between customers and chefs.
- Encapsulation protects information from being seen by outsiders.
- RESTful (Respresentational State Transfer) APIs is a software "architectural style" that is widely-used and scalable. RESTful APIs conform to five constraints/principles:
  - Client-server interface: client and server are independent and communicate through this interface, with either side able to be replaced with the same interface.
  - Stateless: every request is independent and complete, with no dependence on previous requests or the session.
  - Cacheable: can cache on server or client side to improve performance.
  - Layered system: multiple layers in system in order to hide the actual logic/resources.
  - Uniform interface: interface stays the same to decouple client and server logic.
- HTTP protocol (HyperText Transfer Protocol) is an implementation of REST style. HTTP has different types of service request methods (analogous to "service counters"):
  - GET for reading data
  - POST for creating data
  - PUT for updating data (complete update)
  - PATCH for updating data (partial update/modification)
  - DELETE for deleting data
- HTTP status codes are returned in every response from the server under the HTTP protocol. They tell the frontend client about the status of their request.
  - 200 OK is returned for a successful GET, PUT, or PATCH request.
  - 201 Created is returned for a successful POST request.
  - 204 No Content is returned for a successful DELETE request.
  - 400 Bad Request is returned when there's a problem with the request, e.g. a JSON syntax error.
  - 401 Unauthorized is returned when the authentication details are missing/invalid.
  - 403 Forbidden is returned when the requested resource is forbidden.
  - 404 Not Found is returned when the requested resource doesn't exist.
- CRUD stands for create, read, update, and delete - the majority of actions needed for web applications. CRUD describes the lifecycle of database record management.
- Most APIs communicate using JSON, although some use XML.
- Open APIs are third party APIs open to public use.
- Flask and Django are two web frameworks that can be used to easily build web applications.

