#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    args_count == len(argv)
    arg_message = 'arguement'
    if args_count > 1:
        arg_message = arg_message + 's'
    if args_count > 0:
        print(f"{args_count} {arg_message}:")
        for i in argv:
            print(f"{i + 1} {argv[i]}")
    else:
        print(f"{args_count} {arg_message}.")
