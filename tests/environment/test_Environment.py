from unittest import TestCase

from src.environment.Environment import Environment
from src.environment.EnvironmentType import EnvironmentType


class TestEnvironment(TestCase):
    def setUp(self):
        self.environment = Environment()

    def test_production_constants_assert_equals(self):
        self.environment.set_environment(EnvironmentType.PRODUCTION)
        hr_thoughts = "hr-thoughts"
        en_thoughts = "en-thoughts"
        thought_path = "assets/thoughts.json"
        backup_thought_path = "backups"
        view_loading_message = "Loading production environment.."
        self.assertEqual(hr_thoughts, self.environment.get().THOUGHT_COLLECTION_HR)
        self.assertEqual(en_thoughts, self.environment.get().THOUGHT_COLLECTION_EN)
        self.assertEqual(thought_path, self.environment.get().LOCAL_THOUGHT_PATH)
        self.assertEqual(backup_thought_path, self.environment.get().LOCAL_BACKUP_PATH)
        self.assertEqual(view_loading_message, self.environment.get().MESSAGE_LOADING)

    def test_staging_constants_assert_equals(self):
        self.environment.set_environment(EnvironmentType.STAGING)
        hr_thoughts_staging = "hr-thoughts-staging"
        en_thoughts_staging = "en-thoughts-staging"
        thought_path_staging = "assets/thoughts-staging.json"
        backup_thought_path_staging = "backups-staging"
        view_loading_message_staging = "Loading staging environment.."
        self.assertEqual(hr_thoughts_staging, self.environment.get().THOUGHT_COLLECTION_HR)
        self.assertEqual(en_thoughts_staging, self.environment.get().THOUGHT_COLLECTION_EN)
        self.assertEqual(thought_path_staging, self.environment.get().LOCAL_THOUGHT_PATH)
        self.assertEqual(backup_thought_path_staging, self.environment.get().LOCAL_BACKUP_PATH)
        self.assertEqual(view_loading_message_staging, self.environment.get().MESSAGE_LOADING)
