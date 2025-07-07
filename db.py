from sqlalchemy import create_engine
import config

db_engine = create_engine(config.DATABASE_URL)