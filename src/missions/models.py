from flask                         import current_app
from flask_security.models         import fsqla_v3                                               as fsqla
from sqlalchemy.orm                import DeclarativeBase,MappedAsDataclass,Mapped,mapped_column
from sqlalchemy_imageattach.entity import Image,image_attachment

class MedalRibbon(current_app.database.Model):
    __tablename__ = "medal_ribbons"
    name:        Mapped[str] = mapped_column(prinamry_key=True)
    image:       Mapped[str] = mapped_column(unique=True) #URL to the image
    description: Mapped[str]

class Mission(current_app.database.Model):
    __tablename__ = "missions"
    name:        Mapped[str] = mapped_column(primary_key=True)
    description: Mapped[str]
    ribbon:      Mapped[str] = mapped_column(ForeignKey(medal_ribbons.name,onupdate="CASCADE",ondelete="CASCADE"),nullable=False,unique=True)

class MissionObjective(current_app.database.Model):
    __tablename__ = "mission_objectives"
    mission:    Mapped[str]  = mapped_column(ForeignKey(missions.name,onupdate="CASCADE",ondelete="CASCADE"),nullable=False,unique=True)
    objective:  Mapped[str]
    achieved:   Mapped[bool]

class CrewRibbon(current_app.database.Model):
    __tablename__ = "crew_ribbons"
    id:       Mapped[int] = mapped_column(primary_key=True)
    nickname: Mapped[str] = mapped_column(ForeignKey(crew_members.nickname,onupdate="CASCADE",ondelete="CASCADE"),nullable=False)
    ribbon:   Mapped[str] = mapped_column(ForeignKey(medal_ribbons.name,onupdate="CASCADE",ondelete="CASCADE"),nullable=False)

class ShipRibbon(current_app.database.Model):
    __tablename__ = "ship_ribbons"
    id:     Mapped[int] = mapped_column(primary_key=True)
    ribbon: Mapped[str] = mapped_column(ForeignKey(medal_ribbons.name,onupdate="CASCADE",ondelete="CASCADE"),nullable=False)

current_app.user_datastore = SQLAlchemyUserDatastore(current_app.database,User,Role)

current_app.database.create_all()
