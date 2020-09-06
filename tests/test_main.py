import os
import sys

from click.testing import CliRunner

from kondense import main
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_main():
    runner = CliRunner()
    result = runner.invoke(main, 'kondense/demo.txt')
    print(result)
    print(result.output)
    assert result.exit_code == 0
