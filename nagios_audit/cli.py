import click
from presentation import Presentation

@click.command()
@click.option('--file', default='status.dat', help='Location of the nagios.stat file.')
def main(file):
    """Auditing tool for Nagios"""
    presentation_obj = Presentation(file)
    presentation_obj.printAll()


if __name__ == '__main__':
    main()
