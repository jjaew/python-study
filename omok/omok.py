# 쉬프트 에프육 이름바꾸기
# 컨트롤 알트 엘 자동 줄맞춤
# 컨트롤 슬레쉬 드래그한거 싹다 주석처리

class omok:
    def __init__(self):
        self.board = [[" " for i in range(19)] for j in range(19)]
        self.start()
        self.gameover = False

    def start(self):
        print("시작!!!")

    def end(self):
        print("게임 끝!!!")

    def winner(self, color, x, y):
        left_dir = [[-1, 0], [0, -1], [-1, 1], [-1, -1]]
        right_dir = [[1, 0], [0, 1], [1, -1], [1, 1]]

        for i in range(4):
            kx, ky = x, y
            left, right = 0, 0

            for k in range(4):
                if self.board[kx + left_dir[i][0]][ky + left_dir[i][1]] == color:
                    left += 1
                    kx += left_dir[i][0]
                    ky += left_dir[i][1]
                else:
                    break

            kx, ky = x, y

            for k in range(4):
                if self.board[kx + right_dir[i][0]][ky + right_dir[i][1]] == 'B':
                    right += 1
                    kx += right_dir[i][0]
                    ky += right_dir[i][1]
                else:
                    break

            if left + right == 4:
                self.gameover = True

                if color == 'B':
                    print("검은돌 승리!!!")
                else:
                    print("흰돌 승리!!!")

                return

    def print_board(self):
        for i in range(19):
            print(self.board[i])

    def put_stone(self, color, x, y):
        if self.is_blank(x, y):
            self.board[x][y] = color
            self.winner(color, x, y)
        else:
            print("좌표를 다시 선택하세요!!!")
            return False

        self.print_board()
        return True

    def is_blank(self, x, y):
        if self.board[x][y] is " ":
            return True
        return False


# class stone:
#     def __init__(self, color, x, y):
#         self.color = color
#         self.x = x
#         self.y = y


game = omok()

turn = True

while not game.gameover:
    color = ''
    if turn:
        print("black turn")
        color = "B"
    else:
        print("white turn")
        color = "W"

    x, y = map(int, input().split())

    if game.put_stone(color, x, y):
        turn = not turn
