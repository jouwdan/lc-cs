"""These small teaching functions assume integer inputs."""
def gcd_iterative(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def gcd_recursive(a, b):
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

if __name__ == "__main__":
    print(gcd_iterative(48, 18))
    for a, b, expected in [(7,0,7),(0,7,7),(18,48,6),(6,6,6),(-48,18,6),(0,0,0)]:
        assert gcd_iterative(a,b) == gcd_recursive(a,b) == expected
