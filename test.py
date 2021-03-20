from prompt_toolkit import prompt


class chess_piece:
    file = "a"
    rank = "1"
    file_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
    rank_list = ["1", "2", "3", "4", "5", "6", "7", "8"]

    def place(self, position):
        file = position[0]
        rank = position[1]
        if not (file in self.file_list) and not (rank in self.rank_list):
            print("invalid position")
            self.file=None
            self.rank=None
            return [self.file, self.rank]

        self.file = file
        self.rank = rank
        return [self.file, self.rank]

    def up(self, position):
        file = position[0]
        rank = position[1]

        if not (rank in self.rank_list) or self.rank_list[-1] == rank:
            # print('invalid position')
            return [file, rank]
        current_rank = rank
        for i in range(0, len(self.rank_list)):
            self.rank_list[i]

            if self.rank_list[i] == current_rank:
                return [file, self.rank_list[i + 1]]

        pass

    def down(self, position):
        file = position[0]
        rank = position[1]

        if not (rank in self.rank_list) or self.rank_list[0] == rank:
            # print('invalid position')
            return [file, rank]
        current_rank = rank
        for i in range(0, len(self.rank_list)):
            self.rank_list[i]

            if self.rank_list[i] == current_rank:
                return [file, self.rank_list[i - 1]]

        pass

    def right(self, position):
        file = position[0]
        rank = position[1]

        if not (file in self.file_list) or self.file_list[-1] == file:
            # print('invalid position')
            return [file, rank]
        current_file = file
        for i in range(0, len(self.file_list)):
            self.file_list[i]

            if self.file_list[i] == current_file:
                return [self.file_list[i + 1], rank]

        pass

    def left(self, position):
        file = position[0]
        rank = position[1]

        if not (file in self.file_list) or self.file_list[0] == file:
            # print('invalid position')
            return [file, rank]
        current_file = file
        for i in range(0, len(self.file_list)):
            self.file_list[i]

            if self.file_list[i] == current_file:
                return [self.file_list[i - 1], rank]

        pass


class pawn(chess_piece):
    def move_list(self):
        original_postion = [self.file, self.rank]
        possible_moves = []

        current_postion = original_postion
        new_postion = self.up(current_postion)

        if not new_postion == current_postion:
            possible_moves.append(new_postion)

        return possible_moves


class rook(chess_piece):
    def move_list(self):
        possible_moves = []

        up_list = self.up_list()
        down_list = self.down_list()
        right_list = self.right_list()
        left_list = self.left_list()

        possible_moves = right_list + left_list + up_list + down_list

        return possible_moves

    def up_list(self):
        original_postion = [self.file, self.rank]
        possible_moves = []

        current_postion = original_postion
        new_postion = self.up(current_postion)

        while not new_postion == original_postion:
            new_postion = self.up(current_postion)
            if not new_postion == current_postion:
                possible_moves.append(new_postion)
                current_postion = new_postion
            else:
                break

        return possible_moves

    def down_list(self):
        original_postion = [self.file, self.rank]
        possible_moves = []

        current_postion = original_postion
        new_postion = self.down(current_postion)

        while not new_postion == original_postion:
            new_postion = self.down(current_postion)
            if not new_postion == current_postion:
                possible_moves.append(new_postion)
                current_postion = new_postion
            else:
                break

        return possible_moves

    def right_list(self):
        original_postion = [self.file, self.rank]
        possible_moves = []

        current_postion = original_postion
        new_postion = self.right(current_postion)

        while not new_postion == original_postion:
            new_postion = self.right(current_postion)
            if not new_postion == current_postion:
                possible_moves.append(new_postion)
                current_postion = new_postion
            else:
                break

        return possible_moves

    def left_list(self):
        original_postion = [self.file, self.rank]
        possible_moves = []

        current_postion = original_postion
        new_postion = self.left(current_postion)

        while not new_postion == original_postion:
            new_postion = self.left(current_postion)
            if not new_postion == current_postion:
                possible_moves.append(new_postion)
                current_postion = new_postion
            else:
                break

        return possible_moves


class bishop(chess_piece):
    def move_list(self):
        possible_moves = []

        up_right_list = self.up_right_list()
        down_right_list = self.down_right_list()
        up_left_list = self.up_left_list()
        down_left_list = self.down_left_list()

        possible_moves = up_right_list + down_right_list + up_left_list + down_left_list

        return possible_moves

    def up_right_list(self):
        original_postion = [self.file, self.rank]
        possible_moves = []

        current_postion = original_postion

        new_rank = self.up(current_postion)[1]
        if new_rank == current_postion[1]:
            return possible_moves
        new_file = self.right(current_postion)[0]
        if new_file == current_postion[0]:
            return possible_moves

        new_postion = [new_file, new_rank]

        while not new_postion == original_postion:
            new_rank = self.up(current_postion)[1]
            if new_rank == current_postion[1]:
                break
            new_file = self.right(current_postion)[0]
            if new_file == current_postion[0]:
                break

            new_postion = [new_file, new_rank]

            if not new_postion == current_postion:
                possible_moves.append(new_postion)
                current_postion = new_postion
            else:
                break

        return possible_moves

    def down_right_list(self):
        original_postion = [self.file, self.rank]
        possible_moves = []

        current_postion = original_postion

        new_rank = self.down(current_postion)[1]
        if new_rank == current_postion[1]:
            return possible_moves
        new_file = self.right(current_postion)[0]
        if new_file == current_postion[0]:
            return possible_moves

        new_postion = [new_file, new_rank]

        while not new_postion == original_postion:
            new_rank = self.down(current_postion)[1]
            if new_rank == current_postion[1]:
                break
            new_file = self.right(current_postion)[0]
            if new_file == current_postion[0]:
                break

            new_postion = [new_file, new_rank]

            if not new_postion == current_postion:
                possible_moves.append(new_postion)
                current_postion = new_postion
            else:
                break

        return possible_moves

    def up_left_list(self):
        original_postion = [self.file, self.rank]
        possible_moves = []

        current_postion = original_postion

        new_rank = self.up(current_postion)[1]
        if new_rank == current_postion[1]:
            return possible_moves
        new_file = self.left(current_postion)[0]
        if new_file == current_postion[0]:
            return possible_moves

        new_postion = [new_file, new_rank]

        while not new_postion == original_postion:
            new_rank = self.up(current_postion)[1]
            if new_rank == current_postion[1]:
                break
            new_file = self.left(current_postion)[0]
            if new_file == current_postion[0]:
                break

            new_postion = [new_file, new_rank]

            if not new_postion == current_postion:
                possible_moves.append(new_postion)
                current_postion = new_postion
            else:
                break

        return possible_moves

    def down_left_list(self):
        original_postion = [self.file, self.rank]
        possible_moves = []

        current_postion = original_postion

        new_rank = self.down(current_postion)[1]
        if new_rank == current_postion[1]:
            return possible_moves
        new_file = self.left(current_postion)[0]
        if new_file == current_postion[0]:
            return possible_moves

        new_postion = [new_file, new_rank]

        while not new_postion == original_postion:
            new_rank = self.down(current_postion)[1]
            if new_rank == current_postion[1]:
                break
            new_file = self.left(current_postion)[0]
            if new_file == current_postion[0]:
                break

            new_postion = [new_file, new_rank]

            if not new_postion == current_postion:
                possible_moves.append(new_postion)
                current_postion = new_postion
            else:
                break

        return possible_moves


class queen(rook, bishop):
    def move_list(self):
        possible_moves = []

        up_list = self.up_list()
        down_list = self.down_list()
        right_list = self.right_list()
        left_list = self.left_list()
        up_right_list = self.up_right_list()
        down_right_list = self.down_right_list()
        up_left_list = self.up_left_list()
        down_left_list = self.down_left_list()

        possible_moves = (
            right_list
            + left_list
            + up_list
            + down_list
            + up_right_list
            + down_right_list
            + up_left_list
            + down_left_list
        )

        return possible_moves


class knight(chess_piece):
    def move_list(self):
        possible_moves = []

        up_list = self.up_list()
        down_list = self.down_list()
        right_list = self.right_list()
        left_list = self.left_list()

        possible_moves = up_list + down_list + right_list + left_list

        return possible_moves

    def up_list(self):
        original_postion = [self.file, self.rank]
        possible_moves = []

        current_postion = original_postion

        new_position = self.up(current_postion)
        if new_position == current_postion:
            return possible_moves

        current_postion = new_position

        new_position = self.up(current_postion)
        if new_position == current_postion:
            return possible_moves

        current_postion = new_position

        new_position = self.right(current_postion)
        if not new_position == current_postion:
            possible_moves.append(new_position)

        new_position = self.left(current_postion)
        if not new_position == current_postion:
            possible_moves.append(new_position)

        return possible_moves

    def down_list(self):
        original_postion = [self.file, self.rank]
        possible_moves = []

        current_postion = original_postion

        new_position = self.down(current_postion)
        if new_position == current_postion:
            return possible_moves

        current_postion = new_position

        new_position = self.down(current_postion)
        if new_position == current_postion:
            return possible_moves

        current_postion = new_position

        new_position = self.right(current_postion)
        if not new_position == current_postion:
            possible_moves.append(new_position)

        new_position = self.left(current_postion)
        if not new_position == current_postion:
            possible_moves.append(new_position)

        return possible_moves

    def right_list(self):
        original_postion = [self.file, self.rank]
        possible_moves = []

        current_postion = original_postion

        new_position = self.right(current_postion)
        if new_position == current_postion:
            return possible_moves

        current_postion = new_position

        new_position = self.right(current_postion)
        if new_position == current_postion:
            return possible_moves

        current_postion = new_position

        new_position = self.up(current_postion)
        if not new_position == current_postion:
            possible_moves.append(new_position)

        new_position = self.down(current_postion)
        if not new_position == current_postion:
            possible_moves.append(new_position)

        return possible_moves

    def left_list(self):
        original_postion = [self.file, self.rank]
        possible_moves = []

        current_postion = original_postion

        new_position = self.left(current_postion)
        if new_position == current_postion:
            return possible_moves

        current_postion = new_position

        new_position = self.left(current_postion)
        if new_position == current_postion:
            return possible_moves

        current_postion = new_position

        new_position = self.up(current_postion)
        if not new_position == current_postion:
            possible_moves.append(new_position)

        new_position = self.down(current_postion)
        if not new_position == current_postion:
            possible_moves.append(new_position)

        return possible_moves


class king(chess_piece):
    def move_list(self):
        possible_moves = []

        up_list = self.up_list()
        down_list = self.down_list()
        right_list = self.right_list()
        left_list = self.left_list()
        up_right_list = self.up_right_list()
        down_right_list = self.down_right_list()
        up_left_list = self.up_left_list()
        down_left_list = self.down_left_list()

        possible_moves = (
            right_list
            + left_list
            + up_list
            + down_list
            + up_right_list
            + down_right_list
            + up_left_list
            + down_left_list
        )

        return possible_moves

    def up_right_list(self):
        original_postion = [self.file, self.rank]
        possible_moves = []

        current_postion = original_postion

        new_rank = self.up(current_postion)[1]
        if new_rank == current_postion[1]:
            return possible_moves
        new_file = self.right(current_postion)[0]
        if new_file == current_postion[0]:
            return possible_moves

        new_postion = [new_file, new_rank]
        possible_moves.append(new_postion)

        return possible_moves

    def down_right_list(self):
        original_postion = [self.file, self.rank]
        possible_moves = []

        current_postion = original_postion

        new_rank = self.down(current_postion)[1]
        if new_rank == current_postion[1]:
            return possible_moves
        new_file = self.right(current_postion)[0]
        if new_file == current_postion[0]:
            return possible_moves

        new_postion = [new_file, new_rank]
        possible_moves.append(new_postion)

        return possible_moves

    def up_left_list(self):
        original_postion = [self.file, self.rank]
        possible_moves = []

        current_postion = original_postion

        new_rank = self.up(current_postion)[1]
        if new_rank == current_postion[1]:
            return possible_moves
        new_file = self.left(current_postion)[0]
        if new_file == current_postion[0]:
            return possible_moves

        new_postion = [new_file, new_rank]
        possible_moves.append(new_postion)

        return possible_moves

    def down_left_list(self):
        original_postion = [self.file, self.rank]
        possible_moves = []

        current_postion = original_postion

        new_rank = self.down(current_postion)[1]
        if new_rank == current_postion[1]:
            return possible_moves
        new_file = self.left(current_postion)[0]
        if new_file == current_postion[0]:
            return possible_moves

        new_postion = [new_file, new_rank]
        possible_moves.append(new_postion)

        return possible_moves

    def up_list(self):
        original_postion = [self.file, self.rank]
        possible_moves = []

        current_postion = original_postion
        new_postion = self.up(current_postion)
        if new_postion == current_postion:
            return possible_moves
        possible_moves.append(new_postion)

        return possible_moves

    def down_list(self):
        original_postion = [self.file, self.rank]
        possible_moves = []

        current_postion = original_postion
        new_postion = self.down(current_postion)
        if new_postion == current_postion:
            return possible_moves

        possible_moves.append(new_postion)

        return possible_moves

    def right_list(self):
        original_postion = [self.file, self.rank]
        possible_moves = []

        current_postion = original_postion
        new_postion = self.right(current_postion)
        if new_postion == current_postion:
            return possible_moves
        possible_moves.append(new_postion)

        return possible_moves

    def left_list(self):
        original_postion = [self.file, self.rank]
        possible_moves = []

        current_postion = original_postion
        new_postion = self.left(current_postion)
        if new_postion == current_postion:
            return possible_moves
        possible_moves.append(new_postion)

        return possible_moves


piece_dictionary = {
    "p": pawn(),
    "b": bishop(),
    "n": knight(),
    "r": rook(),
    "q": queen(),
    "k": king(),
}

piece = prompt("Please enter letter of piece (P,B,N,R,Q,K): ").lower()
file = prompt("Please enter piece's file (a-h): ").lower()
rank = prompt("Please enter piece's rank (1-8): ").lower()

test = piece_dictionary[piece]
test.place([file, rank])

print(test.move_list())
