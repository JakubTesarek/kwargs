# Kwargs
Kwargs is the only True python micro-framework that doesn't limit your creativity™.

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