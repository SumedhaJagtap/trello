from trello import Trello

if __name__ == '__main__':
    trello_app = Trello()

    name, email = 'user1', 'user1@abc.com'
    users1_id = trello_app.add_user(name, email)

    name, email = 'user2', 'user2@abc.com'
    users2_id = trello_app.add_user(name, email)

    name, email = 'user3', 'user3@abc.com'
    users3_id = trello_app.add_user(name, email)

    name, email = 'user4', 'user4@abc.com'
    users4_id = trello_app.add_user(name, email)

    print(trello_app.users.to_string())

    board_name = 'work@tech'
    worktech_board = trello_app.add_board(board_name)
    trello_app.show_board()
    trello_app.show_board(worktech_board)

    trello_app.show_board()

    trello_app.update_board(worktech_board, 'workat.tech', 'PRIVATE')
    trello_app.update_board(worktech_board + 'a', 'workat.tech', 'PRIVATE')  # searching for dummy board
    trello_app.show_board()

    workat_board = trello_app.add_board('workat')
    trello_app.show_board()

    trello_app.add_member_to_board(worktech_board, users1_id)
    trello_app.show_board()

    trello_app.add_member_to_board(worktech_board, users2_id)
    trello_app.add_member_to_board(worktech_board, users3_id)

    trello_app.show_board()
    trello_app.remove_member_from_board(worktech_board, users3_id)
    trello_app.show_board(worktech_board)

    trello_app.delete_board(workat_board)
    trello_app.show_board(workat_board)
    trello_app.show_board()

    mock_interviews_list = trello_app.create_list(worktech_board, 'Mock Interviews')
    trello_app.show_lists(mock_interviews_list)
    trello_app.update_list(mock_interviews_list, 'Mock Interviews - Applied')
    trello_app.show_lists(mock_interviews_list)

    mock_interviews_scheduled_list = trello_app.create_list(worktech_board, 'Mock Interviews - Scheduled')
    trello_app.show_board(worktech_board)

    card1 = trello_app.create_card('ABC',mock_interviews_list)
    card2 = trello_app.create_card('PQR',mock_interviews_list)
    card3 = trello_app.create_card('ERT',mock_interviews_scheduled_list)

    trello_app.show_cards(card1)
    trello_app.show_cards()
    trello_app.show_lists()

    trello_app.delete_list(mock_interviews_list)
    trello_app.show_lists()
    trello_app.show_cards()
