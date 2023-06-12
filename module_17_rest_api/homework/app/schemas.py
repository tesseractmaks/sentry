from marshmallow import Schema, fields, validates, ValidationError, post_load

from crud import get_book_by_title, Book, Author, BOOKS_TABLE_NAME


class BookSchema(Schema):
    book_id = fields.Int(dump_only=True, required=False)
    book_name = fields.Str(required=False)
    author = fields.Int(required=False)

    @validates('book_name')
    def validate_title(self, book_name: str) -> None:

        if get_book_by_title(BOOKS_TABLE_NAME, book_name) is not None:
            raise ValidationError(
                'Book with title "{title}" already exists, '
                'please use a different title.'.format(title=book_name)
            )

    @validates('book_id')
    def validate_book_id(self, data) -> Book:
        return Book(**data)

    @post_load
    def add_book(self, data, **kwargs) -> Book:
        return Book(**data, book_id=None)


# class BookSchemaPatch(Schema):
#     book_id = fields.Int(dump_only=True, required=False)
#     book_name = fields.Str(required=False)
#     author = fields.Int(required=False)
#
#
#
#     @validates('book_name')
#     def validate_title(self, book_name: str) -> None:
#
#         if get_book_by_title(BOOKS_TABLE_NAME, book_name) is not None:
#             raise ValidationError(
#                 'Book with title "{title}" already exists, '
#                 'please use a different title.'.format(title=book_name)
#             )
#
#     @validates('book_id')
#     def validate_book_id(self, data) -> Book:
#         return Book(**data)


class AuthorSchema(Schema):
    author_id = fields.Int(dump_only=True, required=False)
    first_name = fields.Str(required=False)
    last_name = fields.Str(required=False)
    middle_name = fields.Str(required=False)

    @validates('author_id')
    def validate_author_id(self, data) -> Author:
        return Author(**data)


    # @post_load
    # def add_author(self, data, **kwargs) -> Author:
    #     return Author(**data, author_id=None)


# class AuthorSchemaPatch(Schema):
#     author_id = fields.Int(dump_only=True, required=False)
#     first_name = fields.Str(required=False)
#     last_name = fields.Str(required=False)
#     middle_name = fields.Str(required=False)
#
#
#     @validates('author_id')
#     def validate_author_id(self, data) -> Author:
#         return Author(**data)




