import atexit

def main():
    print("Starting the app")

def exit_handler():
    print("Closing the app")

if __name__ == "__main__":
    main()

atexit.register(exit_handler)
