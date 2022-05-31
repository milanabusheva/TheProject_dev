import datetime


class User(object):
    id = int
    name = str
    type = list
    login = str
    password = str
    data_of_registration = datetime.date()
    all_contests = list


class Participant(User):
    id_user = int
    top = int
    teams = list
    contests = list


class Organizer(User):
    id_user = int
    organizer_of_contests = list


class Mentor(User):
    id_user = int
    comand_id = int


class Admin(User):
    id_user = int


class Contest(object):
    id = int

    def __init__(self, proof=bool, id=int):
        self.proof = proof
        if self.proof:
            self.proof_of_whom = id
        else:
            self.by_user = id

    stages = list
    teams = list
    script_autoregistration = list
    applications = list


class Team(object):
    id = int
    leader_id = int
    users_id = list
    mentor_id = int
    project = str
    applications = list
    tickets = list


class Ticket(object):
    id = int
    team_id = int
    contest = int
