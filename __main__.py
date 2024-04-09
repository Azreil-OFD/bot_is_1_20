import sys
from .bot import main
from .test import TestGetRandom
import asyncio

if(len(sys.argv) == 2):
    if(sys.argv[1] == "test"):
       TestGetRandom()
elif __name__ == '__main__':
    asyncio.run(main())
