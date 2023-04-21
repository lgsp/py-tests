import pynecone as pc

config = pc.Config(
    app_name="pycone_test1",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
