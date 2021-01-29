import random
import string
import clipboard
random = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(8)])
clipboard.copy(random)