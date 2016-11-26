import sys
import os

# copy-pasted from "http://stackoverflow.com/a/23386287"

# append module root directory to sys.path
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)
