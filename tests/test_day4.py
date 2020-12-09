from aoc.day4 import validate_hgt


def test_validate_hgt():
    assert not validate_hgt('notvalid')

    assert not validate_hgt('58in')
    assert validate_hgt('59in')
    assert validate_hgt('76in')
    assert not validate_hgt('77in')

    assert not validate_hgt('149cm')
    assert validate_hgt('150cm')
    assert validate_hgt('193cm')
    assert not validate_hgt('194cm')
