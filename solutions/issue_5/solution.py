'''
Issue #5 Solution
----------------------------

Analysis:
import random
import string

def generate_password(length=12):
    '''Generate a secure random password.
    
    Args:
        length (int): Length of the password (default: 12)
        
    Returns:
        str: A secure random password
    '''
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Ensure at least one of each type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill the rest randomly
    all_chars = lowercase + uppercase + digits + special
    password.extend(random.choice(all_chars) for _ in range(length - 4))
    
    # Shuffle the password
    random.shuffle(password)
    return ''.join(password)

# Example usage
if __name__ == "__main__":
    print(generate_password())

Solution:
'''

import random
import string

def generate_password(length=12):
    '''Generate a secure random password.
    
    Args:
        length (int): Length of the password (default: 12)
        
    Returns:
        str: A secure random password
    '''
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Ensure at least one of each type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill the rest randomly
    all_chars = lowercase + uppercase + digits + special
    password.extend(random.choice(all_chars) for _ in range(length - 4))
    
    # Shuffle the password
    random.shuffle(password)
    return ''.join(password)

# Example usage
if __name__ == "__main__":
    print(generate_password())
