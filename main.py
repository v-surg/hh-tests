
from tests import *
import sys


tests_list = [test_smoke,
              test_response_format,
              test_positive_ru,
              test_positive_en,
              test_negative_abracadabra,
              test_negative_special,
              test_consistency,
              test_load]


def main():
    for t in tests_list:
        test_name = f'\'{t.__name__}\''
        try:
            t()
            sys.stdout.write(f'Test {test_name} ok\n')
        except AssertionError as e:
            sys.stderr.write(f'Test {test_name} error: {e}\n')
        except Exception as e:
            sys.stderr.write(f'Test {test_name} unexpected error: {e}\n')


if __name__ == '__main__':
    main()