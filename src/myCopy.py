# Custom implementation of copy module
def __has_and_is_callable(x, attr):
	return hasattr(x, attr) and callable(getattr(x, attr))


def __manual_copy(x):
	out = x.__class__()  # Assume no constructor arguments
	for key, value in x.__dict__.items():
		setattr(out, key, value)
	return out


def copy(x):
	if __has_and_is_callable(x, "__copy__"):
		return x.__copy__()
	if __has_and_is_callable(x, "__deepcopy__"):
		return x.__deepcopy__()
	if __has_and_is_callable(x, "copy"):
		return x.copy()
	if hasattr(x, "__dict__"):
		return __manual_copy(x)
	return x
