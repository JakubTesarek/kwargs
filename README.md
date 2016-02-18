[![Build Status](https://travis-ci.org/JakubTesarek/kwargs.svg?branch=master)](https://travis-ci.org/JakubTesarek/kwargs)

# Kwargs
Kwargs is the only True python micro-framework that doesn't limit your creativity™.

## Requirments
You need [Python >= 3.3](https://travis-ci.org/JakubTesarek/kwargs). You can
probably use it with older versions, including Python 2 but our buid dependecies
don't work in this version so we are not testing it.

## Installation
Kwargs is self-contained so you can simply copy-paste kwargs.py to your project.
We are also working on creating a pypi project. Stay tuned.

## Usage
### Basic usage
```python
from kwargs import App

def my_function():
	# implement your app logic
	return

app = App(my_function)
app.run()
```

`App(my_function)` initializes Kwargs framework with your app logic. You have to
implement this logic yourself. It can do literally anything!

When you want to then execute your code, simply call `app.run()`.

### Shorthand usage (for lead developers)
Kwargs framework strifes for short and easy to read code. Therefore it provides you with shorthand execution. 

```python
from kwargs import run

def my_function():
	# implement your app logic
	return

run(my_function)
```

### Super-short usage (for hackers)
You can also skip initialization of Kwargs framework altogether and execute
the app logic yourself.

```python
def my_function():
	# implement your app logic
	return

my_function()
```

Notice that you don't have to import Kwargs package anymore. It's because in
this example we don't use it at all. Magic!

We don't recommend using this style as it might be confusing for other developers that are not familiar with Kwargs framework. But heck, sometimes you just need to get job done.

## Contributing
- Create a branch. Only I can commit to master because it's my repository.
- Run tests with code coverage `$ py.test --cov=kwargs`
- Run pylint `$ pylint kwargs tests`

## FAQ
### Is Kwargs the right framework for my project?
Kwarks is currently the fastest python framework with minimum overhead and it doesn't
limit usage of other tools and frameworks. As such it fits projects of all sizes.
But it's specially good when you're writing small utility and your manager keeps asking
what framework you use.

### What should do I do when I find a bug?
Before you submit pull request or file a ticket, please search Stack Owerflow. We have more then [36.000 answered questions](http://stackoverflow.com/search?q=kwargs) so you might find help there. If you still think, you find a bug, [file a ticket](https://github.com/JakubTesarek/kwargs/issues) or send a pull request.