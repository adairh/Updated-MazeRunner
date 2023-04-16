# Hàm Minimax
def minimax(state, depth, isMaximizingPlayer):
    # Điểm kết thúc: đạt độ sâu tối đa hoặc trò chơi kết thúc
    if depth == 0 or game_over(state):
        return evaluate(state)
    
    # Lượt chơi của bot
    if isMaximizingPlayer:
        best_value = -float('inf')
        for action in available_actions(state):
            child_state = apply_action(state, action)
            value = minimax(child_state, depth - 1, False)
            best_value = max(best_value, value)
        return best_value
    
    # Lượt chơi của đối thủ
    else:
        best_value = float('inf')
        for action in available_actions(state):
            child_state = apply_action(state, action)
            value = minimax(child_state, depth - 1, True)
            best_value = min(best_value, value)
        return best_value
    
# Hàm game_over
def is_game_over(state, time_limit):
    # Check if the time has run out
    if state['time_remaining'] <= 0 or time_limit <= 0:
        return True
    
    # Check if the enemy bot is killed
    enemy_bot_killed = True
    for bot in state['bots']:
        if bot['name'] != state['bot']['name'] and bot['is_alive']:
            enemy_bot_killed = False
            break
    if enemy_bot_killed:
        return True
    
    # Game is not over
    return False


# Hàm available_actions
def available_actions(state):
    bot = state.bots[state.turn]
    enemy_bot = state.bots[1 - state.turn]

    # Kiểm tra xem bot địch có gần hơn đồng xu so với bot mình không
    enemy_distance_to_coins = []
    for coin in state.coins:
        distance = manhattan_distance((enemy_bot.x, enemy_bot.y), (coin.x, coin.y))
        enemy_distance_to_coins.append(distance)
    min_enemy_distance = min(enemy_distance_to_coins)

    # Tìm đồng xu gần nhất với bot mình
    my_distance_to_coins = []
    for coin in state.coins:
        distance = manhattan_distance((bot.x, bot.y), (coin.x, coin.y))
        my_distance_to_coins.append(distance)
    min_my_distance = min(my_distance_to_coins)

    # Tạo danh sách các hành động có thể thực hiện
    actions = []
    for direction in ['North', 'South', 'West', 'East']:
        action = Action(bot.name, direction)
        new_state = apply_action(state, action)

        # Nếu địch gần đồng xu hơn mình thì đi ra giữa map
        if min_enemy_distance < min_my_distance:
            if not is_stuck(new_state):
                actions.append(action)

        # Nếu mình gần đồng xu hơn thì ăn đồng xu
        else:
            if action.action_type == ActionType.MOVE:
                if (bot.x, bot.y) in [(coin.x, coin.y) for coin in new_state.coins]:
                    actions.append(action)

    # Nếu không thể ăn được đồng xu thì vẫn đi ra giữa map để tránh bị kẹt
    if not actions:
        for direction in ['North', 'South', 'West', 'East']:
            action = Action(bot.name, direction)
            new_state = apply_action(state, action)
            if not is_stuck(new_state):
                actions.append(action)

    return actions