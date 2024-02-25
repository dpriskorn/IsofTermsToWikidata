import logging
import os

from pydantic import BaseModel

from models.source import Source

logger = logging.getLogger(__name__)


class PublicOrgHandler(BaseModel):
    # read and parse the data into objects
    # use the 3rd level directory names as name for the organization
    # store the filepath for debugging
    path: str = "data/Offentlig_verksamhet"
    sources: list[Source] = list()

    def find_all_sources(self):
        for tuple in os.walk(self.path):
            # We assume all files in the whole tree are sources
            for file in tuple[2]:
                path = os.path.join(tuple[0], file)
                self.sources.append(Source(path=path, name=file))
        logger.info(f"Found {len(self.sources)} sources")

    def iterate_sources(self):
        for source in self.sources:
            source.start()

    def start(self):
        self.find_all_sources()
        input("Press enter to iterate")
        self.iterate_sources()
