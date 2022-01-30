import pygame

pygame.init()


# TODO: implement checks
class Player:

    turn = 0

    def __init__(self, board, color):
        self.board = board
        self.color = color
        self.selected = None
        self.king = self.board.get_square(1, 5).piece if self.color == 'White' else self.board.get_square(8, 5).piece
        self.legal_moves = {}
        self.set_legal_moves()

    def set_legal_moves(self):
        limit = (1, 3) if self.color == 'White' else (7, 9)
        for i in range(limit[0], limit[1]):
            for j in range(1, 9):
                print(self.board.get_square(i, j).piece)
                self.legal_moves[self.board.get_square(i, j).piece] = []

    def get_legal_moves(self):
        for piece in self.legal_moves:
            self.legal_moves[piece] = piece.possible_moves()

    def clear_legal_moves(self):
        for piece in self.legal_moves:
            self.legal_moves[piece] = []

    def highlight_legal_moves(self, piece):
        for move in self.legal_moves[piece]:
            move.highlighted = not move.highlighted

    def play(self, x, y):

        # if self.king.in_check():
        #     if king in double check
        #         calculate king moves
        #         if no king moves
        #             checkmate
        #         if king moves
        #             add king moves
        #     if not in double check
        #         find moves for all pieces
        #         if no moves
        #             checkmate
        #         if moves:
        #             add moves
        # if not in check
        #     calculate moves and add

        self.get_legal_moves()

        sq = self.board.get_clicked_square(x, y)
        # print(sq)
        # print(self.legal_moves)
        if self.selected is not None:
            if sq in self.legal_moves[self.selected]:
                self.selected.move(sq)
                Player.turn ^= 1

            self.highlight_legal_moves(self.selected)
            self.selected = None
            self.clear_legal_moves()
        else:
            self.selected = sq.piece
            # print(sq)
            if self.selected is not None and self.selected.color != self.color:
                self.selected = None
            if self.selected is not None:
                # self.legal_moves = self.selected.possible_moves()
                self.highlight_legal_moves(self.selected)
