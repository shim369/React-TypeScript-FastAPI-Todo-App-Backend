from decouple import config
import motor.motor_asyncio

MONOGO_API_KEY = config('MONOGO_API_KEY')

client = motor.motor_asyncio.AsyncIOMotorClient(MONOGO_API_KEY)
database = client.API_DB
collection_todo = database.todo
collection_user = database.user
