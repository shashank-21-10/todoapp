from dotenv import load_dotenv
import os, pathlib

basedir = pathlib.Path()
basedir = os.path.join(str(basedir.cwd()) , 'src' , '.env')

load_dotenv(basedir)

DATABASE_URL = os.getenv("DATABASE_URL")