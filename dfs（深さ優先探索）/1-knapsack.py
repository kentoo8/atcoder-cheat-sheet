n_items = 10
max_weight = 20
weights = [1, 3, 2, 6, 5, 9, 10, 11, 20, 3]
values = [4, 20, 1, 5, 6, 2, 3, 4, 5, 5]

"""
ナップサック問題:
  max_weight を超えないitemたちをナップサックに詰めるとき、valueの合計値が最大になる選び方と、その時のvalueは？
"""


def get_best_items(weights, values, max_weight):
    """条件を満たす最適なアイテムの選び方とその時の合計valueを返す"""
    # 状態
    best_state = {"value": 0, "weight": 0, "item_indices": []}

    # DFS
    def choose_items_dfs(
        current_item_index,
        current_weight,
        current_value,
        current_item_indices,
    ):
        """現在の状態以降から、最適なitemの選び方を全探索する"""
        # 終了条件
        if current_item_index == n_items:
            if current_value > best_state["value"]:
                best_state["value"] = current_value
                best_state["weight"] = current_weight
                best_state["item_indices"] = current_item_indices.copy()

            # debug
            print(current_weight, current_value, current_item_indices)
            return

        # ステップを進める
        ## 0: current_item_indexのアイテムを選ばない場合
        choose_items_dfs(
            current_item_index=current_item_index + 1,
            current_weight=current_weight,
            current_value=current_value,
            current_item_indices=current_item_indices,
        )

        ## 1: 選ぶ場合
        next_weight = current_weight + weights[current_item_index]
        next_value = current_value + values[current_item_index]

        if next_weight <= max_weight:
            current_item_indices.append(current_item_index)
            choose_items_dfs(
                current_item_index=current_item_index + 1,
                current_weight=next_weight,
                current_value=next_value,
                current_item_indices=current_item_indices,
            )
            current_item_indices.pop()

    # 探索実行
    choose_items_dfs(
        current_item_index=0,
        current_weight=0,
        current_value=0,
        current_item_indices=[],
    )
    return best_state


best_items = get_best_items(weights=weights, values=values, max_weight=max_weight)

print()
print(best_items)
