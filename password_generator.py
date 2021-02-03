import random
import string
import clipboard


def pass_generator():
    random_pass = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(8)])
    copy_in_buffer = clipboard.copy(random_pass)
    return copy_in_buffer
