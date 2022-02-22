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

    def winner(self, winner):
        print("승리자는 " + winner)

    def print_board(self):
        for i in range(19):
            print(self.board[i])

    def put_stone(self, color, x, y):
        if self.is_blank(x,y):
            self.board[x][y] = color
        else:
            print("좌표를 다시 선택하세요!!!")

        self.print_board()

    def is_blank(self,x,y):
        if self.board[x][y] is " ":
            return True
        return False


# class stone:
#     def __init__(self, color, x, y):
#         self.color = color
#         self.x = x
#         self.y = y


game = omok()

while game.gameover is False:
    color = input()
    x = int(input())
    y = int(input())

    game.put_stone(color,x,y)
