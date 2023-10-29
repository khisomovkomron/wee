
API_HOSTS = {
    "dev_wee": "",
    "stage_wee": "",
    "prod_wee": "https://wee.ae",

}


DB_HOST = {
    'machine1': {
        "test": {"host": "localhost",
                 "database": "",
                 "table_prefix": "",
                 "socket": None,
                 "port": 10005
                 },
        "dev": {
            "host": "host.docker.internal",
            "database": "local",
            "table_prefix": "wp_",
            "socket": None,
            "port": 10005
        },
        "prod": {
            "host": "host.docker.internal",
            "database": "local",
            "table_prefix": "wp_",
            "socket": None,
            "port": 10005
        },
    },
    'docker': {
        "test": {
            "host": "host.docker.internal",
            "database": "",
            "table_prefix": "",
            "socket": None,
            "port": 10005
        },
        "dev": {
            "host": "host.docker.internal",
            "database": "local",
            "table_prefix": "",
            "socket": None,
            "port": 10005
        },
        "prod": {
            "host": "host.docker.internal",
            "database": "local",
            "table_prefix": "",
            "socket": None,
            "port": 10005
        },
    }
}