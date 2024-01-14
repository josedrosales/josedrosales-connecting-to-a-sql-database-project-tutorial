
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
# 1) Connect to the database here using the SQLAlchemy's create_engine function
db_host = os.getenv("localhost")
db_user = os.getenv("josedrosales")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")


# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function

# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function

# 4) Use pandas to print one of the tables as dataframes using read_sql function
