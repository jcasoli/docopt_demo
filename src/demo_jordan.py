# author: Jordan Casoli
# date: 2020-01-15

"""This script prints out docopt args.
Usage: demo.py <arg1> --arg2=<arg2> [--arg3=<arg3>] [<arg4>]

Options:
<arg>             Takes any value (this is a required positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)
[<arg4>]          Takes any value (this is an optional positional argument)
""" 
from docopt import docopt

opt = docopt(__doc__)
# define main function
def main():
    # code for "guts" of script goes here
    print(opt)
    print(opt["<arg4>"])
    print(type(opt))
# code for other functions & tests goes here

# call main function
if __name__ == "__main__":
    main()




