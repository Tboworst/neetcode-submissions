class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # hash for O(1) lookup
        # check rows
        for i in range(9):
            # create an empty set for each row
            s = set()
            # go over the columns
            for j in range(9):
                item = board[i][j]
                # if the item is already in the set
                if item in s:
                    return False
                elif item != '.':
                    # meaning if the item is a number
                    s.add(item)

        # check columns
        for i in range(9):
            # create an empty set for each column
            s = set()
            for j in range(9):
                # check 1 column at a time, so it's j, i
                item = board[j][i]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)

        starts = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]

        for i, h in starts:
            s = set()
            for row in range(i, i+3):
                for col in range(h, h+3):
                    item = board[row][col]
                    if item in s:
                        return False
                    elif item != '.':
                        s.add(item)

        return True
'''
Input:Board-> 9x9 sudoku board
if boards is empty meaningn no value in baord

Valid - if row and column 1-9 
each of the subboxes must contain the digits 1-9 without duplicates 

Goal:Return trie the sudolu board is vlaid otherwise false

Approach:
hash = set()
Loop through row 



'''