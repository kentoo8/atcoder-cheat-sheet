def get_binary_sequences(length):
    """
    0, 1からなる指定長のリスト全体を返す
    itertools.product の手作り版
    """
    sequences = []
    sequence = []

    def collect_sequence_dfs():
        def is_complete():
            return len(sequence) == length

        def append_sequence():
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
