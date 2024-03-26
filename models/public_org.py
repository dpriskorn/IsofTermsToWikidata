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

    def gather_and_print_statistics(self):
        total_term_line_count = 0
        total_term_count = 0
        for source in self.sources:
            for term in source.terms:
                total_term_count += 1
                total_term_line_count += term.raw_line_count
        print(
            f"Found {len(self.sources)} sources with a total of "
            f"{total_term_count} terms and "
            f"{total_term_line_count} term lines in total."
        )

    def start(self):
        self.find_all_sources()
        self.iterate_sources()
        self.gather_and_print_statistics()
        # input("Press enter to iterate")
