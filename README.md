# trello
machine coding solution for Trello

>Problem statement : https://workat.tech/machine-coding/practice/trello-problem-t0nwwqt61buz


### Class: Trello
- Attributes:
  - ID
  - URL
  - CreationDate
  - Boards: List of boards
  - Users: List of users
- Methods:
  - add_board
  - add_user

### Class:User
- Attributes:
  - ID
  - Name 
  - Email


### Class: Board
- Attributes:
  - ID
  - Name
  - Privacy (Public/Private)
  - URL
  - Members : List of Users
- Methods:
  - create()
  - delete()
  - add_members()


### Class: List
- Attributes:
  - ID 
  - Name 
  - Cards: List of Cards
  - URL
- Methods:
  - create()
  - delete() -> delete all cards as well

### Class: Card
- Attributes:
  - ID
  - Name
  - Desc
  - Assignee
  - URL
- Methods:
  - assign_user()
  - unassign_user()