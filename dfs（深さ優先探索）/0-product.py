def get_binary_sequences(length: int) -> list[list[int]]:
    """
    0, 1からなる指定長のリスト全体を返す
    itertools.product の手作り版
    """
    sequences: list[list[int]] = []
    sequence: list[int] = []

    def collect_sequence_dfs() -> None:
        def is_complete() -> bool:
            return len(sequence) == length

        def append_sequence() -> None:
            sequences.append(sequence.copy())

        if is_complete():
            append_sequence()
            return

        for value in (0, 1):
            sequence.append(value)
            collect_sequence_dfs()
            sequence.pop()

    collect_sequence_dfs()
    return sequences


sequences = get_binary_sequences(length=5)
for sequence in sequences:
    print(sequence)
