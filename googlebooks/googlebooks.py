from google.oauth2 import service_account
from googleapiclient.discovery import build

def fetch_books(startIndex=0, maxResults=1):
    SERVICE_ACCOUNT_FILE = 'googlebooks/google-apis.json'

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=['https://www.googleapis.com/auth/books']
    )

    service = build('books', 'v1', credentials=credentials)
    request = service.volumes().list(source='public', q='*', maxResults=maxResults, startIndex=startIndex)
    response = request.execute()
    return data(response)    

def data(response):
    books = []

    for book in response.get('items', []):
        book_info = {
            'id': book['id'],
            'title': book['volumeInfo'].get('title', ''),
            'subtitle': book['volumeInfo'].get('subtitle', ''),
            'authors': book['volumeInfo'].get('authors', []),
            'publisher': book['volumeInfo'].get('publisher', ''),
            'published_date': book['volumeInfo'].get('publishedDate', ''),
            'description': book['volumeInfo'].get('description', ''),
            'categories': book['volumeInfo'].get('categories', ['']),
            'thumbnail': book['volumeInfo'].get('imageLinks', {}).get('thumbnail', '')
        }
        books.append(book_info)

    return books