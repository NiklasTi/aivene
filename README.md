# Aivene API

Aivene offers an innovative search engine for your AI and LLM, leveraging advanced AI to enable seamless search, query generation, and comprehensive search results aggregation.


## Installation

```
pip install aivene
```


## Quick Start

```
from aivene import Aivene

api_key = "YOUR_API_KEY"
client = Aivene(api_key)

# Search
search_results = client.search("example query")

# Generate Queries
queries = client.generate_queries("example topic")

# Search Queries
combined_search = client.search_from_input("example topic")

```


## Features

* **Search** : Directly search the web with keywords.
* **Generate Queries** : Create search queries from text.
* **Search Queries** : Generate and search queries based on input text.


## Support

For support or inquiries, please visit our contact page.


## License

This project is licensed under the MIT License - see the LICENSE file for details.
