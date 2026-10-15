def run_length_encoding(S: str) -> list[tuple[str, int]]:
    """
    文字列を run-length 圧縮（連長圧縮）する。

    例:
        Input:  "AAABAAAAACC"
        Output: [("A", 3), ("B", 1), ("A", 5), ("C", 2)]
    """
    if not S:
        return []

    ans = []
    current = S[0]
    repeat_count = 1

    for char in S[1:]:
        if current == char:
            repeat_count += 1
        else:
            ans.append((current, repeat_count))
            current = char
            repeat_count = 1

    ans.append((current, repeat_count))

    return ans


print(run_length_encoding("SSSAAACCCCCC"))
