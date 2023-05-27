import shutil
import string
import random
from typing import List

from fastapi import UploadFile
from app.configs.environment import env


class FileManagerService:
    MEDIA_DIR_NAME: str = env.media_dir_name
    FILE_NAME_LENGTH: int = int(env.file_name_length)

    @classmethod
    def get_obfuscated_filename(cls, filename: str) -> str:
        extension = filename.split('.')[::-1][0]
        new_file_name = "".join(random.choices(string.ascii_lowercase+string.digits, k=cls.FILE_NAME_LENGTH))
        return f"{new_file_name}.{extension}"

    @classmethod
    def store_as(cls, uploaded_file: UploadFile, filepath: str) -> None:
        direct_path = f"../{cls.MEDIA_DIR_NAME}/{filepath}/{cls.get_obfuscated_filename(uploaded_file.filename)}"
        with open(direct_path, "wb") as buffer:
            shutil.copyfileobj(uploaded_file.file, buffer)

    @classmethod
    def store_multiple_as(cls, uploaded_files: List[UploadFile], filepath: str) -> None:
        for uploaded_file in uploaded_files:
            direct_path = f"../{cls.MEDIA_DIR_NAME}/{filepath}/{cls.get_obfuscated_filename(uploaded_file.filename)}"
            with open(direct_path, "wb") as buffer:
                shutil.copyfileobj(uploaded_file.file, buffer)
