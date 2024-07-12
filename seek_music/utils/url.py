from typing import Text


def join_paths(*paths: Text, startswith: Text = "/") -> Text:
    return startswith + "/".join(path.strip(" /") for path in paths if path.strip(" /"))
