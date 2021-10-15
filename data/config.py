from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
PROVIDER_TOKEN = env.str("Provider_TOKEN")
IP = env.str("ip")

PGUSER = env.str("PGUSER")
PGPASSWORD = env.str("PGPASSWORD")
