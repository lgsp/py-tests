import pynecone as pc

config = pc.Config(
    app_name="my_quiz",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
