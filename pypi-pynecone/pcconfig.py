import pynecone as pc

config = pc.Config(
    app_name="pypi_pynecone",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
