import databases
import ormar
import sqlalchemy

from app.configs.environment import env

database = databases.Database(env.db_url)
metadata = sqlalchemy.MetaData()

class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database
