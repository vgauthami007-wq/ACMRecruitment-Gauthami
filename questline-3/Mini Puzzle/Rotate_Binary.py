def rotate_binary(binary_str: str, k: int) -> int:
    """
    Rotate a binary string k steps to the right,
    then return its decimal value.
    """
    n = len(binary_str)
    k = k % n  # Ensure k is within length
    rotated = binary_str[-k:] + binary_str[:-k]
    return int(rotated, 2)

if __name__ == "__main__":
    b = "1011"   # Binary for 11
    k = 2
    print(f"Original binary: {b}")
    print(f"Rotated {k} steps -> Decimal:", rotate_binary(b, k))

    b = "11001"  # Binary for 25
    k = 3
    print(f"\nOriginal binary: {b}")
    print(f"Rotated {k} steps -> Decimal:", rotate_binary(b, k))
