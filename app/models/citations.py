def attach_citation(summary: str, source_url: str) -> dict:
    """
    Attaches the source URL to the summary as a citation.

    Args:
        summary (str): The summary text
        source_url (str): The original URL of the content

    Returns:
        dict: A dictionary containing the summary and its source
    """
    return {
        "summary": summary,
        "source": source_url
    }
