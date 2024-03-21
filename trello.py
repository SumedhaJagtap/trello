import time
import uuid
import json

import pandas as pd

from user import User
from board import Board
from list import List
from card import Card


class Trello:
    def __init__(self):
        self.trello_id = str(uuid.uuid4())
        self.creation_time = time.time()
        self.url = None
        self.boards = pd.DataFrame(columns=['board_id', 'name', 'privacy', 'url', 'members'])
        self.boards.set_index('board_id', inplace=True)
        self.users = pd.DataFrame(columns=['user_id', 'username', 'email', 'is_active', 'is_admin'])
        self.users.set_index('user_id', inplace=True)
        self.lists = pd.DataFrame(columns=['list_id', 'name', 'board_id', 'url'])
        self.lists.set_index('list_id', inplace=True)
        self.cards = pd.DataFrame(columns=['card_id', 'name', 'desc', 'assignee', 'url', 'list_id'])
        self.cards.set_index('card_id', inplace=True)

    def add_user(self, username, email):
        user = User(username, email)
        self.users.loc[user.user_id] = user.__dict__
        print(f'Created User : {user.user_id}')
        return user.user_id

    def add_board(self, name):
        board = Board(name)
        self.boards.loc[board.board_id] = board.__dict__
        print(f'Created Board : {board.board_id}')
        return board.board_id

    def update_board(self, board_id, name, privacy):
        if board_id not in self.boards.index:
            print('No board found')
        else:
            self.boards.loc[board_id, 'name'] = name or self.boards.loc[board_id, 'name']
            self.boards.loc[board_id, 'privacy'] = privacy or self.boards.loc[board_id, 'privacy']

    def add_member_to_board(self, board_id, member):
        # Make a copy of the list of members
        members = self.boards.loc[board_id, 'members'].copy()
        # Check if the member is not already in the list
        if member not in members:
            # Append the member to the copied list
            members.append(member)
            # Assign the modified list back to the DataFrame
            self.boards.loc[board_id, 'members'] = members

    def remove_member_from_board(self, board_id, member):
        # Make a copy of the list of members
        members = self.boards.loc[board_id, 'members'].copy()
        # Check if the member is not already in the list
        if member in members:
            # Append the member to the copied list
            members.remove(member)
            # Assign the modified list back to the DataFrame
            self.boards.loc[board_id, 'members'] = members

    def show_board(self, board_id=None):
        boards = self.boards.copy()
        if board_id:
            if board_id in self.boards.index:
                boards = self.boards.loc[[board_id]]
            else:
                print(f'Board {board_id} does not exist')
                return
        boards.reset_index(inplace=True)
        lists = self.lists.copy()

        # Group df2 by board_id and aggregate the 'name' values into a single list
        grouped_names = lists.groupby('board_id')['name'].apply(list).reset_index()

        merged_data = pd.merge(boards, grouped_names, on='board_id', how='left')
        merged_data.rename(columns={'name_y': 'lists'}, inplace=True)

        print(json.dumps(merged_data.to_dict(orient='records')))

    def delete_board(self, board_id):
        if board_id in self.boards.index:
            self.boards = self.boards.drop(board_id)

    def create_list(self, board_id, name):
        task_list = List(name, board_id)
        self.lists.loc[task_list.list_id] = task_list.__dict__
        print(f'Created List : {task_list.list_id}')
        return task_list.list_id

    def show_lists(self, list_id=None):

        lists = self.lists.copy()
        if list_id:
            if list_id in self.lists.index:
                lists = self.lists.loc[[list_id]]
            else:
                print(f'lists {list_id} does not exist')
                return
        lists.reset_index(inplace=True)
        cards = self.cards.copy()

        # Group df2 by board_id and aggregate the 'name' values into a single list
        grouped_names = cards.groupby('list_id')['name'].apply(list).reset_index()

        merged_data = pd.merge(lists, grouped_names, on='list_id', how='left')
        merged_data.rename(columns={'name_y': 'cards'}, inplace=True)

        print(json.dumps(merged_data.to_dict(orient='records')))
        # if list_id:
        #     if list_id in self.lists.index:
        #         print(json.dumps(self.lists.loc[list_id].to_dict()))
        #     else:
        #         print(f'List {list_id} does not exist')
        # else:
        #     print(json.dumps(self.lists.to_dict(orient='records')))

    def update_list(self, list_id, name):
        if list_id not in self.lists.index:
            print('No list found')
        else:
            self.lists.loc[list_id, 'name'] = name or self.lists.loc[list_id, 'name']

    def create_card(self, name, list_id):
        card = Card(name, '', list_id, )
        self.cards.loc[card.card_id] = card.__dict__
        print(f'Created Card : {card.card_id}')
        return card.card_id

    def show_cards(self, card_id=None):
        print(card_id)
        if card_id:
            if card_id in self.cards.index:
                print(json.dumps(self.cards.loc[card_id].to_dict()))
            else:
                print(f'Card {card_id} does not exist')
        else:
            print(json.dumps(self.cards.to_dict(orient='records')))

    def delete_list(self, list_id):
        cards = self.cards.copy()
        cards.reset_index(inplace=True)
        cards = cards[cards['list_id'] == list_id]['card_id'].to_list()
        for card_id in cards:
            self.cards = self.cards.drop(card_id)
        self.lists = self.lists.drop(list_id)
