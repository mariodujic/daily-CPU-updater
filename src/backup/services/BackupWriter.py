import os

from src.services.Write import Write


class BackupWriter(Write):
    def __init__(self, local_writer: Write):
        self.local_writer = local_writer

    def write(self, thoughts: list, folder_path: str, file_name: str, encoder):
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        self.local_writer.write(thoughts, folder_path + file_name, encoder)
