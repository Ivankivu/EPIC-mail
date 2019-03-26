def create_app(config_name):  # pragma: no cover
    app.config.from_object(env_config[config_name])
    app.config.from_pyfile(os.path.join(BASE_DIR, 'config.py'))
    return app