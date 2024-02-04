from pydantic import Field
from pydantic_settings import BaseSettings

class Configuration(BaseSettings):
    env: str = Field(default='dev')

configuration = Configuration();