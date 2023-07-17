from typing import List, Dict


def Articles():
    articles: list[dict[str, int | str] | dict[str, int | str] | dict[str, int | str]] = [
            {
                'id': 1,
                'title': 'Article One',
                'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad asperiores est ipsa obcaecati, provident sunt tempora! Cupiditate deserunt facilis iusto, minus modi nesciunt provident. Ex ipsa iste tempora tempore vitae!',
                'author': 'Kurt Elliott',
                'create_date': '04-25-2023'
            },
            {
                'id': 2,
                'title': 'Article Two',
                'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad asperiores est ipsa obcaecati, provident sunt tempora! Cupiditate deserunt facilis iusto, minus modi nesciunt provident. Ex ipsa iste tempora tempore vitae!',
                'author': 'John Doe',
                'create_date': '04-25-2023'
            },
            {
                'id': 3,
                'title': 'Article Three',
                'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad asperiores est ipsa obcaecati, provident sunt tempora! Cupiditate deserunt facilis iusto, minus modi nesciunt provident. Ex ipsa iste tempora tempore vitae!',
                'author': 'John Smith',
                'create_date': '04-25-2023'
            }
        ]
    return articles