from parsers.template_requests import template_requests
from parsers.data.github_raw_url_list import *
from parsers.data.protocols import *
from parsers.data.replace_proxy import REPLACE_PROXY
from parsers.data.protocol_names import PROTOCOL_NAMES
from typing import List
import logging


logging.basicConfig(level=logging.INFO)

def template_github_raw(url_lst: List[str], protocol: str) -> List[str]:
    """
    Processing the received text from the request to the
    site and bringing it to the standard.
    :param url_lst: The link that the request goes to.
    :param protocol: The protocol of the received proxy list.
    :return: List of IP proxies.
    """
    final_lst = []
    for url in url_lst:
        try:
            response = template_requests(goal_url=url)

            if response is None:
                continue

            text = response.text

            if not text:
                continue

            lines = text.splitlines()
            answer_lines = []
            for ans in lines:
                if REPLACE_PROXY.get(protocol, False):
                    for prot in ALL_PROTOCOLS:
                        if prot in ans:
                            ans = ans.replace(prot, "")
                    ans = protocol + ans
                answer_lines.append(ans)
            final_lst.extend(answer_lines)
        except Exception as e:
            logging.error(f"Error processing {url}: {e}")
    return final_lst

def raw_main() -> None:
    """
    Record each received response according to the protocol in the accompanying document.
    :return: It does not return anything, but only keeps records in the documents.
    """
    for prot in GITHUB_RAW_URL_LIST.keys():
        with open(PROTOCOL_NAMES[prot], "w", encoding="utf-8"):
            pass

    all_proxies = set()
    for protocol, url_lst in GITHUB_RAW_URL_LIST.items():
        proxies = template_github_raw(url_lst, protocol)
        unique_proxies = list(set(proxies))
        with open(PROTOCOL_NAMES[protocol], "a", encoding="utf-8") as f:
            f.write("\n".join(unique_proxies))
        all_proxies.update(unique_proxies)

    with open("all.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(sorted(all_proxies)))


if __name__ == "__main__":
    raw_main()