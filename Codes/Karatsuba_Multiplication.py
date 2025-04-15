## 5. Karatsuba Integer Multiplication
# Algo 1
def karatsuba_multiply(num1_str: str, num2_str: str) -> str:
    """
    Time Complexity: O(n^log3) ≈ O(n^1.585)
    Space Complexity: O(n)
    """
    if len(num1_str) < 4 or len(num2_str) < 4:
        return str(int(num1_str) * int(num2_str))

    n = max(len(num1_str), len(num2_str))
    n2 = n // 2

    num1_str = num1_str.zfill(n)
    num2_str = num2_str.zfill(n)

    a = int(num1_str[:-n2])
    b = int(num1_str[-n2:])
    c = int(num2_str[:-n2])
    d = int(num2_str[-n2:])

    ac = int(karatsuba_multiply(str(a), str(c)))
    bd = int(karatsuba_multiply(str(b), str(d)))
    ab_cd = int(karatsuba_multiply(str(a + b), str(c + d)))

    ad_bc = ab_cd - ac - bd
    result = ac * 10 ** (2 * n2) + ad_bc * 10 ** n2 + bd
    return str(result)

def test_karatsuba_multiply():
    result = karatsuba_multiply("1234", "5678")
    return result

print(test_karatsuba_multiply())

# Algo 2
def karatsuba(num1_str: str, num2_str: str) -> str:
    n = len(num1_str)

    if n==2:
        return str(int(num1_str)*int(num2_str))
    
    n2 = n//2

    a = int(num1_str[:-n2])
    b = int(num1_str[-n2:])
    c = int(num2_str[:-n2])
    d = int(num2_str[-n2:])

    S1 = int(karatsuba(str(a), str(c)))
    S2 = int(karatsuba(str(b), str(d)))
    S3 = int(karatsuba(str(a+b), str(c+d)))

    return str(int(S1*pow(10, n) + (S3-S1-S2)*pow(10, 0.5*n) + S2))

print(karatsuba("1234","5678"))