from flask import Flask, request
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
api = Api(app)

BOOKS_TABLE_NAME = "books"
AUTHORS_TABLE_NAME = "author"


@api.route('/api/books', '/api/books/<int:book_id>')
class Books(Resource):
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


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
