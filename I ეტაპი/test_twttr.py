from twttr import shorten


def test_empty():
    assert shorten("") == ""

def test_upper():
    assert shorten("NIKA") == "NK"
    assert shorten("DARWIN") == "DRWN"
    assert shorten("KUMISI") == "KMS"

def test_lower():
    assert shorten("nika") == "nk"
    assert shorten("darwin") == "drwn"
    assert shorten("kumisi") == "kms"

def main():
    test_empty()
    test_upper()
    test_lower()

if __name__ == "__main__":
    main()