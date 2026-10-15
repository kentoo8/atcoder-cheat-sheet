N = 3


def evaluate(state: int) -> int:
    """現在の状態を答えとして評価する。"""
    return state


def is_finished(step: int) -> bool:
    """すべての要素について判断し終えたか。"""
    return step == N


def make_next_state(state: int, step: int) -> int:
    """step 番目の値を選んだ場合の次の状態を作る。"""
    return state + step


def choose_best(results: list[int]) -> int:
    """子の探索結果から最良のものを選ぶ。"""
    return max(results)


def dfs(
    step: int,
    state: int,
) -> int:
    """
    step 以降について探索し、
    この状態から得られる最大値を返す。
    """

    # 終了条件
    if is_finished(step):
        return evaluate(state)

    results = []

    # step を選ばない
    result = dfs(
        step + 1,
        state,
    )
    results.append(result)

    # step を選ぶ
    next_state = make_next_state(state, step)
    result = dfs(
        step + 1,
        next_state,
    )
    results.append(result)

    # 子の結果をまとめて親へ返す
    return choose_best(results)


ans = dfs(
    step=0,
    state=0,
)

print(ans)
