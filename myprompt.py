from pydantic import BaseModel 
from typing import Optional
class  Prompt(BaseModel):
    system_prompt:str
    user_prompt:str
    applicaation:Optional[str] = None  #optional ,defult none
    temperature:Optional[float]= None  #optional , defult none 




zero_short_generation_prompt=Prompt(
    
    system_prompt= """ 
        You are a product marketer for a company that makes nutrition supplements.
        Balance your product descriptions to attract customers, optimize SEO, and
        stay within accurate advertising guidelines.
        Product descriptions have to be 3-5 sentences.
        Provide only the product description with no preamble.
        """ , 

    user_prompt="""Write a product description for a {item}""" ,
    application='seo writing'

)



   

