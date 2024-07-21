# 0x00. Pagination

## Resources
* <https://intranet.alxswe.com/rltoken/7Kdzi9CH1LdSfNQ4RaJUQw>
* <https://intranet.alxswe.com/rltoken/tfzcEbTSdMYSYxsspJH_oA>

## Learning Objectives
* How to paginate a dataset with simple page and page_size parameters
* How to paginate a dataset with hypermedia metadata
* How to paginate in a deletion-resilient manner

### e.g. a function named index_range that takes two integer arguments page and page_size
```
def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for a pagination range.

    Args:
    page (int): The current page number (1-indexed).
    page_size (int): The number of items per page.

    Returns:
    tuple: A tuple containing the start index and the end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)

# Example usage
page = 2
page_size = 10
print(index_range(page, page_size))  # Output: (10, 20)

```

### Explanation
* Start Index: The start index is calculated as `(page - 1) * page_size`. This gives the position in the list where the current page starts.
* End Index: The end index is calculated as `start_index + page_size`. This gives the position in the list where the current page ends.
	
-> For example, if `page` is 2 and `page_size` is 10:

* The start index would be `(2 - 1) * 10 = 10`.
* The end index would be `10 + 10 = 20`.

-> This means that for page 2 with a page size of 10, the items to be displayed are those from index 10 to index 19 (inclusive).
