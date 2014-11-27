import logging
import sys

from . import Genderize, GenderizeException

logging.basicConfig(level=logging.WARNING)

g = Genderize()
returncode = 0  # no error
for line in sys.stdin:
    name = line.strip()
    try:
        data = g.get1(name)
        print("{data[name]}: {data[gender]}".format(data=data))
    except GenderizeException:
        returncode = 1  # at least one lookup failed
        logging.error("Couldn't look up gender for %r", name, exc_info=True)

exit(returncode)
