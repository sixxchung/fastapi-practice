from fastapi import FastAPI
from fastapi import APIRouter
router = APIRouter(prefix='/blog', tag=['blog'])
@router.get('/')

from routers import blog

app = FastAPI()
app.include_router(blog.router)


@app.get('/')
def index():
    return {'message': 'Hello world!'}

from typing import Optional

@app.get(
    '/blog/all', 
    tags=['blog'],
    summary='Retrieve all blogs',
    description = 'the api call simulates fetching all blogs'
    response_description='the lis of available blogs')
def get_all_blogs(page, page_size=16, numoftag:Optional[int]=None):  
    return {'msg': f'All {page_size} blogs on page {page}'}

@app.get(
    '/blog/{id}/{comment_id}',
    tags=['blog', 'comment'])
def get_comment(id:int, comment_id:int, valid:bool=True, username:Optional[str]=None):
    """
    Retriving a comment of this blogs 
    - **id** mandatory
    - **valid** optional 
    """
    return {'msg': f'{id}...'}

from enum import Enum
class BlogType(str, Enum):
    short='short'
    story='story'
    howto='howto'

@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):   # predefind path using Enum
    return {'message':f"Blog type is {type}"}

from fastapi import status, Response
from urllib import response
@app.get('/blog/{id}', status_code=status.HTTP_404_NOT_FOUND)  # path parameter
def get_blog(id:int, response:Response ):
    if id < 6 :
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'err':f'Blog id {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'msg':f"Blog id with {id}"}




