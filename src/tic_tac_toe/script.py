def clear_console():
	print("\n" * 3)


def update_board_ui(board_data):
	board_ui_str = "  1 2 3\n"
	for row in range(1, 4):
		board_ui_str += str(row) + " "
		for col in range(1, 4):
			result = next((cell for cell in board_data if cell["row"] == row and cell["col"] == col), None)
			if result:
				board_ui_str += result["symbol"]
			else:
				board_ui_str += " "
			board_ui_str += "|"
		board_ui_str += '\n'
	print(board_ui_str)


def get_players_info():
	while True:
		try:
			player1_name = input("player 1, please enter your name: ").strip()
			if not player1_name:
				raise ValueError("name cannot be empty. please try again.")
			player1_symbol = input("player 1, please enter your symbol (X/O) or 'q' to quit: ").upper()
			if player1_symbol not in ["X", "O", "Q"]:
				raise ValueError("invalid symbol. please choose X, O, or Q.")
			player2_name = input("player 2, please enter your name: ").strip()
			if not player2_name:
				raise ValueError("name cannot be empty. please try again.")
			if player1_symbol == "Q":
				player2_symbol = input("player 2, please enter your symbol (X/O) or 'q' to quit: ").upper()
				if player2_symbol not in ["X", "O", "Q"]:
					raise ValueError("invalid symbol. please choose X, O, or Q.")
				player1_symbol = "X" if player2_symbol == "O" else "O"
			else:
				player2_symbol = "X" if player1_symbol == "O" else "O"

			return (player1_name, player1_symbol), (player2_name, player2_symbol)
		except ValueError as e:
			print(f"error: {e}")


def check_if_player_won(board_data) -> int or None:
	check_rows = [[] for _ in range(3)]
	check_cols = [[] for _ in range(3)]
	check_diagonals = [[] for _ in range(2)]
	for row in range(1, 4):
		for col in range(1, 4):
			for cell in board_data:
				if cell["row"] == row and cell["col"] == col:
					check_rows[row - 1].append(cell["player_num"])
					check_cols[col - 1].append(cell["player_num"])
					if row == col:
						check_diagonals[0].append(cell["player_num"])
					elif row + col == 4:
						check_diagonals[1].append(cell["player_num"])

	possible_wins = check_rows + check_cols + check_diagonals
	for i in range(len(possible_wins)):
		if len(possible_wins[i]) == 3:
			are_all_items_similar = all(item == possible_wins[i][0] for item in possible_wins[i])
			if are_all_items_similar:
				return possible_wins[i][0]
	return None


def tic_tac_toe_gameplay():
	(player1_name, player1_symbol), (player2_name, player2_symbol) = get_players_info()
	board_data = []
	current_player = 1
	for i in range(9):
		player_won_num = check_if_player_won(board_data)
		if player_won_num:
			clear_console()
			update_board_ui(board_data)
			player_won_name = player1_name if player_won_num == 1 else player2_name
			print(player_won_name + " won!")
			return
		# switch player except on start
		if len(board_data):
			current_player = 1 if current_player == 2 else 2
		while True:
			try:
				current_player_name = player1_name if current_player == 1 else player2_name
				current_player_symbol = player1_symbol if current_player == 1 else player2_symbol

				clear_console()
				update_board_ui(board_data)
				print(current_player_name + " turn.")
				player_choice_row = int(input("Select row (1-3): "))
				player_choice_col = int(input("Select column (1-3): "))

				# check if input within board range
				if player_choice_row < 1 or player_choice_row > 3 or player_choice_col < 1 or player_choice_col > 3:
					print("Invalid input, please try again.")
					continue

				player_choice_cell = {
					"player_num": current_player,
					"row": player_choice_row,
					"col": player_choice_col,
					"symbol": current_player_symbol
				}
				# check if cell is taken
				if any(cell["row"] == player_choice_cell["row"] and cell["col"] == player_choice_cell["col"] for cell in
					   board_data):
					print("Cell already taken! Try again.")
					continue
				# update board
				board_data.append(player_choice_cell)
				break
			except ValueError:
				print("invalid input, enter only numbers")
				continue
	print("Game over with Tie!")


def run_game():
	while True:
		tic_tac_toe_gameplay()
		play_again = input("Play again? (y/n): ")
		if play_again.lower() != "y":
			break


run_game()
