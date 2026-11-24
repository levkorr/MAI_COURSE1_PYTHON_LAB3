import argparse
import sys
from .errors import MediaLibError

def parse_help():
    ''' Модуль выводящий help при аргументе --help

    Args:
        None

    Returns:
        None
    '''
    if "--help" in sys.argv:
        print("""
        Streamstats - csv and jsonl file streaming analyzer

        Commands:
            analyze                     Main command for file analysis

        Arguments:
            INPUT [INPUT, ...]          Input file paths
        
        Options:
            --format FORMAT [FORMAT, ...]       File formats (required)
            --output FILE                       Save JSON report to FILE
                                                (if is not present, prints to terminal)
            --skip-invalid                      Skip invalid events instead of stopping
        
        Support:
            Analysis of multiple files
            CSV and JSONL files
            CSV delimiters: ',', ';', TAB
            ISO 8601 timestamps
            Levels: DEBUG, INFO, WARNING, ERROR, CRITICAL

        Stats:
            Total number of events
            Number of events by level
            Number of events by source
            Top-k ERROR/CRITICAL sources
            First and last timestamps
            Number of invalid lines (for --skip-invalid)
    
        Examples of working programs:
            python -m streamstats analyze INPUT --format jsonl csv
            python -m streamstats analyze INPUT1 INPUT2 --format jsonl csv --output REPORT.json
            python -m streamstats analyze INPUT --format csv --skip-invalid
        """)
        sys.exit(0)


def parse():
    ''' Модуль создающий парсер

    Args:
        None

    Returns:
        args: Аргументы парсера
    '''
    parser = argparse.ArgumentParser(
        prog="streamstats",
        description="Combines the files.",
        usage="streamstats <command> [arguments]",
        add_help=False
    )
    commands = parser.add_subparsers(dest="command")

    # Для команды analyze
    parse_analyze = commands.add_parser("analyze")
    parse_analyze.add_argument("inputs", nargs="+")
    parse_analyze.add_argument(
        "--format", dest="formats", nargs="+", required=True)
    parse_analyze.add_argument("--output", dest="report_path", required=False)
    parse_analyze.add_argument("--skip-invalid", action="store_true")

    # Аргументы парсера
    args = parser.parse_args()
    return args


def main():
    ''' Являетсе единственным входом и выходом программы
    Обрабатывает ввод в CLI, входные аргументы
    Отвечает за запуск нужных функций
    Хранит основную логику analyze

    Args:
        None

    Returns:
        None

    Raises:
        StreamstatsError: При ожидаемой ошибке
    '''

if __name__ == "__main__":
    try:
        main()
        sys.exit(0)
    except MediaLibError as e:
        print(f"Expected error: {e}", file=sys.stderr)
        sys.exit(2)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(2)
