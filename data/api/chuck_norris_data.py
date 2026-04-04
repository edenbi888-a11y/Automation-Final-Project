


CHUCK_BASE_URL = "https://api.chucknorris.io/jokes/"

RANDOM_PATH =    "/random"
SEARCH_PATH=     "/search"
CATEGORIES_PATH   = "/jokes/categories"
STATUS_CODE_OK  =   200
JOKE_VALUE      =   "value"


   
ALL_CATEGORIES = ['animal', 'career', 'celebrity', 'dev', 'explicit', 'fashion', 'food', 'history', 'money',
 'movie', 'music', 'political', 'religion', 'science', 'sport', 'travel']

# רשימת קטגוריות צפויות (לאימות)
EXPECTED_CATEGORIES = [
    "animal", "career", "celebrity", "dev", "explicit", "fashion", 
    "food", "history", "money", "movie", "music", "political", 
    "religion", "science", "sport", "travel"
]

#Parametrize
SEARCH_QUERIES = [
    ("money",True),
    ("python",False),
    ("kick",True),
    ("courses",False),
    ("food",True),
    ("hotel",True)
]

ERROR_MESSAGES = {
    "short_query": "search query must be at least 3 characters",
    "invalid_category": "category not found"
}