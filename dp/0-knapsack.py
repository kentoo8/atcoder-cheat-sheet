# https://atcoder.jp/contests/abc032/tasks/abc032_d
import sys
from functools import cache

input = sys.stdin.readline


def read_integers() -> list[int]:
    """整数列を1行読み込み、リストとして返す"""
    return list(map(int, input().split()))


def read_int_matrix(n_rows: int) -> list[list[int]]:
    """整数列をn_rows行読み込み、2次元リストとして返す"""
    return [read_integers() for _ in range(n_rows)]


def solve_knapsack(value_weights: list[list[int]], max_weight: int) -> int:
    n_items = len(value_weights)

    @cache
    def get_max_value_from(item_index: int, remaining_weight: int) -> int:
        """item_index番目以降のアイテムだけを使って、残り容量 remaining_weight で得られる最高valueを返す"""

        if item_index == n_items:
            return 0  # 選べるアイテムが残っていない

        current_value, current_weight = value_weights[item_index]

        # アイテムを選ばない場合
        max_value_without_item = get_max_value_from(
            item_index=item_index + 1, remaining_weight=remaining_weight
        )

        # アイテムを選ぶ場合
        if current_weight <= remaining_weight:
            max_value_with_item = current_value + get_max_value_from(
                item_index=item_index + 1,
                remaining_weight=remaining_weight - current_weight,
            )
        else:
            max_value_with_item = 0

        return max(max_value_without_item, max_value_with_item)

    return get_max_value_from(item_index=0, remaining_weight=max_weight)


def main() -> None:
    n_items, max_weight = read_integers()
    value_weights = read_int_matrix(n_items)

    ans = solve_knapsack(value_weights=value_weights, max_weight=max_weight)
    print(ans)


if __name__ == "__main__":
    main()
