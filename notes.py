import datetime
from sqlalchemy import String, Integer, Boolean, Column, ARRAY, ForeignKey
from sqlalchemy.orm import relationship
import sqlalchemy.ext.declarative as dec
import sqlalchemy.orm as orm
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import Session

SQLAlchemyBase = dec.declarative_base()


class User(SQLAlchemyBase):
    id: int
    name: str
    type: list
    login: str
    password: str
    all_contests: list


class Participant(User):
    id_user: int
    top: int
    teams: list
    contests: list


class Admin(User):
    id_user: int


class Contest(SQLAlchemyBase):
    __tablename__ = 'contest'

    id = Column('id', UUID, server_default=sqlalchemy.text('gen_random_uuid()'), primary_key=True)
    proof = Column('proof', Boolean, ForeignKey("user.id"))
    teams = Column('teams', ARRAY(item_type=String), ForeignKey("team.id"), nullable=True)
    applications = Column('applications', ARRAY(item_type=String), ForeignKey("team.id"), nullable=True)


class Team(SQLAlchemyBase):
    __tablename__ = 'team'

    id = Column('id', UUID, server_default=sqlalchemy.text('gen_random_uuid()'), primary_key=True)
    leader_id = Column('leader_id', UUID, ForeignKey("user.id"), server_default=sqlalchemy.text('gen_random_uuid()'),
                       primary_key=True)
    users_id = Column('users_id', ARRAY(item_type=Integer), ForeignKey("user.id"), nullable=True)
    project_id = Column('project_id', UUID, ForeignKey("project.id"),
                        server_default=sqlalchemy.text('gen_random_uuid()'),
                        primary_key=True)
    applications = Column('applications', ARRAY(item_type=String), ForeignKey("user.id"), nullable=True)
    tickets = Column('tickets', ARRAY(item_type=Integer), ForeignKey("ticket.id"), nullable=True)


class Ticket(SQLAlchemyBase):
    __tablename__ = 'ticket'

    id = Column('id', UUID, server_default=sqlalchemy.text('gen_random_uuid()'), primary_key=True)
    team_id = Column('team_id', UUID, ForeignKey("team.id"), server_default=sqlalchemy.text('gen_random_uuid()'),
                     primary_key=True)
    contest = Column('contest_id', UUID, ForeignKey("contest.id"), server_default=sqlalchemy.text('gen_random_uuid()'),
                     primary_key=True)


class Project(SQLAlchemyBase):
    __tablename__ = 'project'

    id = Column('id', UUID, server_default=sqlalchemy.text('gen_random_uuid()'), primary_key=True)
    team_id = Column('team_id', UUID, ForeignKey("team.id"), server_default=sqlalchemy.text('gen_random_uuid()'),
                     primary_key=True)
    contest = Column('contest_id', UUID, ForeignKey("contest.id"), server_default=sqlalchemy.text('gen_random_uuid()'),
                     primary_key=True)
    ticket_id = Column('ticket_id', UUID, ForeignKey("ticket.id"), server_default=sqlalchemy.text('gen_random_uuid()'),
                       primary_key=True)
    card_for_project = Column('card_for_project', String, primary_key=True)

