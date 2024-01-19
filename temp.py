


 # Ex1. pp 40

def sum(n):
    if n <= 0:
        return 0
    return n + sum(n-1)



if __name__ == "__main__":
    print(sum(4))