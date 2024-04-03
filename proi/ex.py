try:
    # code that may raise an exception
except Exception as e:
    # code to handle the exception
    # It's good practice to log the exception or handle it specifically
    print(f"An error occurred: {e}")
else:
    # code to run if no exceptions were raised
    # This block is optional and can be used for code that should only execute if no errors occurred
finally:
    # code that will always be executed
    # This can be used for cleanup actions that must occur whether an exception was raised or not
