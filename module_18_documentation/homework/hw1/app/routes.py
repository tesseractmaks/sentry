import flasgger
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask, request
from flasgger import APISpec, Swagger
from apispec_webframeworks.flask import FlaskPlugin
from flask_restx import Resource, Api
from marshmallow import ValidationError
from create_base import init_db
from models import (
    get_all_obj,
    get_obj_by_id,
    add_obj,
    update_obj_by_id,
    delete_obj_by_id,
    update_patch_obj_by_id,

)
from schemas import BookSchema, AuthorSchema, BookSchemaPatch, AuthorSchemaPatch

app = Flask(__name__)
app.config['SWAGGER'] = {
    'openapi': '3.0.0'
}
api = Api(app)

spec = APISpec(
    title="BooksList",
    version="1.0.0",
    openapi_version="3.0.3",
    plugins=[
        FlaskPlugin(),
        MarshmallowPlugin(),
    ],
)

BOOKS_TABLE_NAME = "books"
AUTHORS_TABLE_NAME = "author"
# get:
#           tags:
#            - books
#           operationId: getApiBooks
#           responses:
#             200:
#               description: Books data
#               schema:
#                 type: array
#                 items:
#                   $ref: '#/definitions/Book'
#         get:
#           tags:
#            - books
#           operationId: getApiBookApiBookId
#           parameters:
#             - name: book_id
#               in: path
#               schema:
#                 type: integer
#               required: true
#           responses:
#             200:
#               description: Books data
#               schema:
#                 type: array
#                 items:
#                   $ref: '#/definitions/Book'


@api.route('/api/books', '/api/books/<int:book_id>')
class Books(Resource):
    """
            This is an endpoint for ...
            ---
            tags:
            - books
            operationId: getApiBooks
            responses:
              200:
                description: Books data
                schema:
                  type: array
                  items:
                    $ref: '#/definitions/Book'

            # tags:
            # - books

            operationId: getApiBookId
            parameters:
            - name: book_id
              in: path
              schema:
                type: integer
              required: true
            responses:
              200:
                description: Books data
                schema:
                  type: array
                  items:
                    $ref: '#/definitions/Book'
            """
    def get(self, *args, **kwargs) -> tuple[list[dict], int]:
        schema = BookSchema()
        names_column = schema.dump_fields.keys()
        if kwargs.get("book_id"):
            return schema.dump(get_obj_by_id(BOOKS_TABLE_NAME, tuple(names_column), kwargs["book_id"])), 200
        return schema.dump(get_all_obj(BOOKS_TABLE_NAME), many=True), 200

    def post(self) -> tuple[dict, int]:
        data = request.json
        schema = BookSchema()
        try:
            book = schema.load(data)
        except ValidationError as exc:
            return exc.messages, 400
        book = add_obj(BOOKS_TABLE_NAME, book.__dict__)
        return schema.dump(book), 201

    def delete(self, *args, **kwargs) -> tuple[list[dict], int]:
        schema = BookSchema()
        names_column = schema.dump_fields.keys()
        return schema.dump(delete_obj_by_id(BOOKS_TABLE_NAME, tuple(names_column), kwargs.get("book_id"))), 200

    def put(self, *args, **kwarg) -> tuple[list[dict], int]:
        schema = BookSchema()
        data = request.json
        try:
            book = schema.load(data)
        except ValidationError as exc:
            return exc.messages, 400
        book = update_obj_by_id(BOOKS_TABLE_NAME, book.__dict__, kwarg["book_id"])
        return schema.dump(book), 201

    def patch(self, *args, **kwarg) -> tuple[list[dict], int]:
        schema = BookSchemaPatch()

        data = request.json
        try:
            book_obj = schema.load(data)
        except ValidationError as exc:
            return exc.messages, 400
        book = update_patch_obj_by_id(BOOKS_TABLE_NAME, book_obj, kwarg["book_id"])
        return schema.dump(book), 201


@api.route('/api/authors', '/api/authors/<int:author_id>')
class Authors(Resource):
    def get(self, *args, **kwargs) -> tuple[list[dict], int]:
        schema = AuthorSchema()
        names_column = schema.dump_fields.keys()
        if kwargs.get("author_id"):
            return schema.dump(get_obj_by_id(AUTHORS_TABLE_NAME, tuple(names_column), kwargs["author_id"])), 200
        return schema.dump(get_all_obj(AUTHORS_TABLE_NAME), many=True), 200

    def post(self) -> tuple[dict, int]:
        data = request.json
        schema = AuthorSchema()
        try:
            author_obj = schema.load(data)
        except ValidationError as exc:
            return exc.messages, 400
        author = add_obj(AUTHORS_TABLE_NAME, author_obj.__dict__)
        return schema.dump(author), 201

    def delete(self, *args, **kwargs) -> tuple[list[dict], int]:
        schema = AuthorSchema()
        names_column = schema.dump_fields.keys()
        return schema.dump(delete_obj_by_id(AUTHORS_TABLE_NAME, tuple(names_column), kwargs["author_id"])), 200

    def put(self, *args, **kwargs) -> tuple[list[dict], int]:
        schema = AuthorSchema()
        data = request.json
        try:
            author = schema.load(data)
        except ValidationError as exc:
            return exc.messages, 400
        author = update_obj_by_id(AUTHORS_TABLE_NAME, author.__dict__, kwargs["author_id"])
        return schema.dump(author), 201

    def patch(self, *args, **kwargs) -> tuple[list[dict], int]:
        schema = AuthorSchemaPatch()
        data = request.json
        try:
            author_obj = schema.load(data)
        except ValidationError as exc:
            return exc.messages, 400
        author = update_patch_obj_by_id(AUTHORS_TABLE_NAME, author_obj, kwargs["author_id"])
        return schema.dump(author), 201


template = spec.to_flasgger(
    app,
    definitions=[BookSchema, BookSchemaPatch],
)

# swagger = Swagger(app, template=template)

swagger = Swagger(app, template=None, template_file="openapi.yaml")

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
