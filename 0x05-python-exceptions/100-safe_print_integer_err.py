#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as inst:
        import sys
        print("Exception: {}".format(inst), file=sys.stderr)
        return False
    else:
        return True
