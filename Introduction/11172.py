from sys import stdin

def main():
    cases = int(stdin.readline())
    for i in range(cases):
        a, b = map(int, stdin.readline().split())
        if a < b:
            print("<")
        elif a == b:
            print("=")
        else:
            print(">")
main()
