import typer
import ssg.parsers

from ssg.site import Site


def main(source="content", dest="dist", parsers="parsers"):
    config = {"source": source, "dest": dest,
              "parsers": [ssg.parsers.ResourceParser()]}

    Site(**config).build()


typer.run(main)
