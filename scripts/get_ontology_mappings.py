import click
import pandas as pd

from zib_uploader.fetch_data import OntologyMappingsFetcher
from zib_uploader.process_data import OntologyMappingsProcessor


@click.command()
@click.argument('output_filepath', type=click.Path())
def main(output_filepath):
    """
    Fetch ATC ontology mappings from bioportal, process them, and write to
    csv. (Serves as example on how to chain OntologyMappingsFetcher and
    OntologyMappingsProcessor)
    """
    fetcher = OntologyMappingsFetcher()
    processor = OntologyMappingsProcessor()
    data = processor.process(fetcher.fetch())
    pd.DataFrame(data).to_csv(output_filepath, index=False)


if __name__ == '__main__':
    main()
