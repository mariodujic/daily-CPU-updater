from src.environment.EnvironmentType import EnvironmentType


def constant(f):
    def temp_set(self, value):
        raise TypeError

    def temp_get(self):
        return f(self)

    return property(temp_get, temp_set)


class _ConstCommon:
    @constant
    def WRITE_REMOTE_DATA_FAILURE(self):
        return "Failure: No item for today in JSON file"

    @constant
    def WRITE_REMOTE_DATA_SUCCESS(self):
        return "Completed: Pushed new items to a database. Item count: "

    @constant
    def BACKUP_REMOTE_DATA_LOCALLY_FAILURE(self):
        return "Failure: Error while backing up remote data"

    @constant
    def BACKUP_REMOTE_DATA_LOCALY_SUCCESS(self):
        return "Completed: Write remote backup"


class _ConstStaging(_ConstCommon):
    @constant
    def THOUGHT_COLLECTION_HR(self):
        return "hr-thoughts-staging"

    @constant
    def THOUGHT_COLLECTION_EN(self):
        return "en-thoughts-staging"

    @constant
    def LOCAL_THOUGHT_PATH(self):
        return "assets/thoughts-staging.json"

    @constant
    def LOCAL_BACKUP_PATH(self):
        return "backups-staging"

    @constant
    def MESSAGE_LOADING(self):
        return "Loading staging environment.."


class _ConstProduction(_ConstCommon):
    @constant
    def THOUGHT_COLLECTION_HR(self):
        return "hr-thoughts"

    @constant
    def THOUGHT_COLLECTION_EN(self):
        return "en-thoughts"

    @constant
    def LOCAL_THOUGHT_PATH(self):
        return "assets/thoughts.json"

    @constant
    def LOCAL_BACKUP_PATH(self):
        return "backups"

    @constant
    def MESSAGE_LOADING(self):
        return "Loading production environment.."


class Environment(object):
    environment_type = EnvironmentType.STAGING

    @classmethod
    def set_environment(cls, environment_type):
        cls.environment_type = environment_type

    @classmethod
    def get(cls):
        if cls.environment_type == EnvironmentType.STAGING:
            return _ConstStaging()
        else:
            return _ConstProduction()
