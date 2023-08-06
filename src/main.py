from libs.my_lib import power_to, capitalize
import atexit


def main():
    print(f"2**5 = {power_to('2', 5)}")
    print(f"\"capitalize\" is now \"{capitalize('capitalize')}d\"")


def exit_handler():
    print("Closing the app")


if __name__ == "__main__":
    print("Starting the app")
    main()

atexit.register(exit_handler)
