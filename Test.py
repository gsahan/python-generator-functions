import Generator


def test_prefix_generator():
    for i in Generator.Generators().getPrefix(5):
        print(i)

if __name__ == "__main__":
    test_prefix_generator()