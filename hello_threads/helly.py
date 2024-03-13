import time
import threading


def main():
    t = threading.Thread(target=greeter, args=("Michael", 10), daemon=True)
    t.start()

    print("This is other work.")
    print(2 * 2)

    t.join()
    print("Done.")


def greeter(name: str, times: int):
    for n in range(0, times):
        print("{} Hello there {}".format(n, name))
        time.sleep(1)


if __name__ == "__main__":
    main()
