import pynecone as pc

config = pc.Config(
    app_name="plus_or_minus",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
