from src.Main import Main
from src.environment import Environment
from src.environment.EnvironmentType import EnvironmentType

Environment.t = EnvironmentType.PRODUCTION
Main().initialize()
