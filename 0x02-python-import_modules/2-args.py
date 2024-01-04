#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    args_count = len(argv) - 1
    arg_message = 'arguement'
    if args_count > 1:
        arg_message = arg_message + 's'
    if args_count > 0:
        print(f"{args_count} {arg_message}:")
        for i, j in enumerate(argv):
            if i == 0:
                continue
            print(f"{i} {j}")
    else:
        print(f"{args_count} {arg_message}.")
