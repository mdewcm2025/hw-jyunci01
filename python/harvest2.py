def turn(times):
    for i in range(times):
        turn_left()

def new_move(times):
    for i in range(times):
        move()

def harvest_one_row_fixed():
    if object_here():
        take()
    if front_is_clear():
        move()

# 移動到田地起點（左上角）
new_move(1)
turn_left()
new_move(2)
turn(3)  # 面向東

# 採收六列，每列八格
for i in range(6):
    # 採收當前起點格
    if object_here():
        take()

    # 採收剩下的 7 格（因為已經採了第一格）
    for j in range(7):
        harvest_one_row_fixed()

    # 移動到下一列（總共 6 列，只執行 5 次換行）
    if i < 5:
        if i % 2 == 0:
            # 從東向 → 左轉南 → 前進 → 左轉西
            turn(1)
            move()
            turn(1)
        else:
            # 從西向 → 右轉南 → 前進 → 右轉東
            turn(3)
            move()
            turn(3)