from flask_restplus import Api

from .configapi import api as api_config
#from .teams import api as api_teams
#from .users import api as api_users
#from .toolsusergroup import ToolsUserGroup

api2 = Api(
    title='API Poc Flask',
    version='0.1',
    description='API To make a POC for Flask/Konga/Kong',
)

api2.add_namespace(api_config)
#api2.add_namespace(api_teams)
#api2.add_namespace(api_users)
