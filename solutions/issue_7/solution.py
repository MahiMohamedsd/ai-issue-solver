'''
Issue #7 Solution
----------------------------

Analysis:
def is_palindrome(text):
    '''Check if a string is a palindrome.
    
    Args:
        text (str): The string to check
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
    '''
    # Remove spaces and special characters, convert to lowercase
    clean_text = ''.join(c.lower() for c in text if c.isalnum())
    return clean_text == clean_text[::-1]

# Example usage
if __name__ == "__main__":
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "Was it a car or a cat I saw?"
    ]
    for text in test_cases:
        print(f"'{text}' is {'a palindrome' if is_palindrome(text) else 'not a palindrome'}")

Solution:
'''

def is_palindrome(text):
    '''Check if a string is a palindrome.
    
    Args:
        text (str): The string to check
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
    '''
    # Remove spaces and special characters, convert to lowercase
    clean_text = ''.join(c.lower() for c in text if c.isalnum())
    return clean_text == clean_text[::-1]

# Example usage
if __name__ == "__main__":
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "Was it a car or a cat I saw?"
    ]
    for text in test_cases:
        print(f"'{text}' is {'a palindrome' if is_palindrome(text) else 'not a palindrome'}")
