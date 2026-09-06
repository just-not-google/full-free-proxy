import requests
from requests import Response
from requests.exceptions import RequestException
from typing import Dict, Union, Optional
from parsers.data.main_constants import MIN_TIMEOUT, MAX_TIMEOUT
from parsers.data.header_list import HEADERS_LIST
import random


def temp_timeout_and_headers() -> Dict[str, Union[int, Dict]]:
    """
    Parameters for further request to the site.
    :return: Dictionary with timeout and headers.
    """
    return {
        "timeout": random.randint(MIN_TIMEOUT, MAX_TIMEOUT),
        "headers": random.choice(HEADERS_LIST)
    }

def template_requests(goal_url: str) -> Optional[Response]:
    """
    The logic of the request to the site and receiving the final Response object.
    :param goal_url: The link that the request goes to.
    :return: The Response object, if the error is None.
    """
    try:
        response = requests.get(goal_url, **temp_timeout_and_headers())

        if response.status_code == 200:
            return response

        raise RequestException("The site does not provide proxy parsing data.")
    except RequestException as e:
        return None
