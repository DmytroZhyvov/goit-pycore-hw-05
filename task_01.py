def caching_fibonacci():
    """Create and use cache for fibonacci numbers calculation."""

    # Create a dictionary to store calculated fibonacci numbers
    cache = {}

    def fibonacci(n=None):
        """Return fibonacci number using recursion and cache"""

        try:
            # Check if an argument is provided
            if n is None:
                raise ValueError('Argument is required')

            # Check if an argument has integer type
            if not isinstance(n, int):
                raise TypeError('Argument must be an integer')

            # Base cases
            if n <= 0:
                return 0
            elif n == 1:
                return 1

            if n in cache:
                return cache[n]

            # Calculate a fibonacci number
            cache[n] = fibonacci(n-1) + fibonacci(n-2)
            return cache[n]

        except (ValueError, TypeError) as error:
            # Handle validation errors
            print(f"Error: {error}")

    return fibonacci