### contains all the config files 

from pydantic_settings  import BaseSettings 
from pydantic  import ConfigDict

class Appconfig(BaseSettings):
    "centralized configuration management using pydantic"
    "automaically reads enviroment variables , validates types and applies defulat values if missing" 

    ## acess token 
    HUGGING_FACE_ACESS_TOKEN: str
    DEFULT_MODEL:str="Qwen/Qwen2.5-0.5B-Instruct"

    model_config=ConfigDict(
        ##automaticall load enviroment variables from .env file    )
        env_file= ".env",
        env_file_encoding= 'utf-8',
        extra= 'ignore' ## pydantic will throw error if we have mention other variables other then mention on this config class .. but here we dont want that , other keys on .env are ignored here
    )

setting= Appconfig()

if __name__ == '__main__':
    print(setting.HUGGING_FACE_ACESS_TOKEN)
    print(setting.DEFULT_MODEL)