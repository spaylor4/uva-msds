# Module 11: Concurrency & Multithreading

- A **thread** is a program unit that is executed independently of other parts of the program. Each thread is executed for a short amount of time (time slice).
  - If a computer has multiple CPUs, threads can run in parallel.
  - No guarantee about order in which threads run.
- Python's `Thread` class (`from threading import Thread`) used to implement basic concurrency.
  - Create thread using `t = Thread(target = myfunc, args = (...))`, then start thread using `t.start()`.
- When threads share a common object, they can conflict with each other.
  - A **race condition** occurs when the effect of multiple threads on shared data depends on the order in which they are scheduled.
- Can use a **lock object** to control threads that manipulate shared resources, avoiding such problems.
  - `self.lock.acquire()` locks and `self.lock.release()` releases a lock object `self.lock`.
  - Lock before try block, then unlock in finally block to avoid race conditions but not keep  threads locked if try block fails.
  - When a thread acquires a lock, it owns the lock until it calls release. A thread that tries to acquire a lock owned by another thread is temporarility deactivated.
- A deadlock occurs if no thread can proceed because each is waiting for another to do some work.
  - Can use a condition object to have a thread temporarily release a lock and regain it at a later time. Implement along with a condition (e.g. `while` statement) and call `.wait()` to make thread wait until condition is met and allow another thread to acquire the object.
  - Another thread can call `notifyAll()` to unblock other threads waiting on the condition.