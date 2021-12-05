def hasBoardWon(board, drawn_nums):
    for col in board:
        if arrHasWon(col, drawn_nums):
            return True
    rows = list(zip(board[0],board[1],board[2],board[3],board[4]))
    for row in rows:
        if arrHasWon(row, drawn_nums):
            return True
    return False

def arrHasWon(arr, drawn_nums):
    for x in arr:
        if x not in drawn_nums:
            return False
    return True

def nonDrawnNums(board, drawn_nums):
    nonDrawn = []
    for col in board:
        for x in col:
            if x not in drawn_nums:
                nonDrawn.append(x)
    return nonDrawn

def main():
    with open("day4/input") as f:
        lineNum = 0
        boardNum = 0
        board = []
        boards = []
        newlines = 0
        for line in f:
            if lineNum==0:
                draw_order = [int(x) for x in line.split(',')]
            else:
                if line == "\n":
                    newlines +=1
                    if not board:
                        continue
                    else:
                        boards.append(board)
                        board = []
                else:
                    board.append([int(x) for x in line.split()])
            lineNum +=1
        boards.append(board)
    part1(boards, draw_order)
    part2(boards, draw_order)

def part1(boards, draw_order):
    drawn_nums = []
    for num in draw_order:
        drawn_nums.append(num)
        for board in boards:
            if hasBoardWon(board, drawn_nums):
                print(board, drawn_nums)
                print(sum(nonDrawnNums(board, drawn_nums))*drawn_nums[-1:][0])
                return

def part2(boards, draw_order):
    drawn_nums = []
    for num in draw_order:
        drawn_nums.append(num)
        for board in boards:
            if hasBoardWon(board, drawn_nums):
                boards.remove(board)
                if len(boards) == 0:
                    print(sum(nonDrawnNums(board, drawn_nums))*drawn_nums[-1:][0])
                    return

main()