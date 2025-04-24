from unittest.mock import Mock

# Create a mock object
mock_object = Mock()

# Set up the mock object to return a specific value
mock_object.some_method.return_value = 42

# Call the method
result = mock_object.some_method()

# Verify the result
print(result)  # Output: 42

# Verify that the method was called
mock_object.some_method.assert_called_once()
