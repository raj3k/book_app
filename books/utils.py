
from typing import List, Dict, Any
import requests
from requests import RequestException, Response
from .models import Book, Author



def get_books_from_google_api(query_arg: str = "hobbit") -> List[Book]:
    for i in range(0, _generate_total_items_number(), 40):
        queries = {"q": query_arg, "startIndex": str(i), "maxResults": "10"}
        books_volume_url = f"https://www.googleapis.com/books/v1/volumes"
        books: List[Book] = []

        try:
            google_response: Response = requests.get(books_volume_url, params=queries)
        except RequestException as e:
            print(f"Encountered error while requesting to google, more info: {e.args}")
            return []
        else:
            if google_response.status_code in range(200, 299):
                results: Dict[str, Any] = google_response.json()
                for item in results.get("items", []):
                    books.append(_build_book_from_item(item))
            else:
                print(f"Request of {google_response.url} has status {google_response.status_code}")
    return books


def _build_book_from_item(item: Dict[str, Any]) -> Book:
    book_info: Dict[str, Any] = item["volumeInfo"]
    authors: List[Author] = [Author.objects.update_or_create(first_names=" ".join(author.split()[:-1]), last_name=author.split()[-1])[0] for author in book_info.get("authors", [])]
    book = Book.objects.update_or_create(
        title = book_info.get("title"),
        publication_date = book_info.get("publishedDate", ""),
        isbn = [x["identifier"] if x["type"] == "ISBN_10" else "" for x in book_info["industryIdentifiers"]][0] if book_info.get("industryIdentifiers") else "",
        pages_count = book_info.get("pageCount", None),
        cover_url = book_info["imageLinks"]["thumbnail"] if book_info.get("imageLinks") else "",
        pub_language = book_info.get("language"),
    )[0]
    print(book)
    book.authors.set([author.id for author in authors])
    return book


def _generate_total_items_number(query_arg: str = "hobbit") -> int:
    books_volume_url = f"https://www.googleapis.com/books/v1/volumes?q={query_arg}"
    google_response: Response = requests.get(books_volume_url)
    return google_response.json()["totalItems"]

