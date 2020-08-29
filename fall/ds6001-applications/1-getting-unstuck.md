# Module 1: Getting Yourself Unstuck

Readings: [Python Data Science Handbook](https://learning.oreilly.com/library/view/python-data-science/9781491912126/) Ch.1, [Stack Overflow's Toxicity Problem](https://atom-morgan.github.io/blog/2018-06-07-stackoverflows-toxicity-problem/), [Suffering on Stack Overflow](https://medium.com/@Aprilw/suffering-on-stack-overflow-c46414a34a52)

### IPython

- Typing a function/method and `?` will return the docstring, and `??` will return the source code (unless the source code is written in C or another language).
- IPython magic commands use `%` to operate on a single line and `%%` to operate on multiple lines of input.
  - `%run myscript.py` runs a py file in IPython.
  - `%timeit` gives the execution time for a line of code.
  - `%debug` opens an interactive debugging session.
  - There are many other magic commands, and you can define your own.
- IPython stores commands run in a list `In` and the output results in a dictionary `Out`.
  - Commands that return None have no output added to `Out`.
  - To suppress output & not store it in `Out`, you can add a semi-colon to the end of a line of code.
- Can execute shell commands in IPython by prefixing with `!`.
  - Ex: can save contents of current working directory using `contents = !ls` (contents will be a special type of shell list).
  - Can pass python variables into shell commands using `{varname}`, e.g. `!ls {path_string_var}`.
  - Shell commands are executed in a temporary subshell, so magic commands are sometimes needed to change things. For example `%cd` will change the working directory, but `!cd` will not.
- When timing code, `%%timeit` times the repeated execution of code, while `%%time` times a single execution.
  - Repeating an operation can sometimes skew the timing, such as sorting a previously-sorted list.
- Can profile code to see which statements take the most time using `%prun` or `%lprun`. `%lprun` does line-by-line profiling and requires `%load_ext line_profiler` (might need to `pip install line_profiler` first.
- Similarly, can profile memory usage with `%memit` and `%mprun` using the `memory_profiler` IPython extension.

### Stack Overflow

- Stack Overflow can be elitist and unwelcoming to beginners, but it is a widely-used resource.
- When asking questions, be sure to provide details on context, code, things you've tried to resolve the problem, etc. Make sure you've done your due diligence and the question hasn't been asked previously.