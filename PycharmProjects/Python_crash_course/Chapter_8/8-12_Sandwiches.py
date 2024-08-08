def make_sandwich(*fillings):
    """Summarise the sandwich we are about to make"""
    print(f"\nMaking a sandwich with the following fillings:")
    for filling in fillings:
        print(f"\t-{filling}")

make_sandwich('ham','cheese')
make_sandwich('cheese', 'tomato', 'lettuce')
make_sandwich('egg', 'mayonnaise')
make_sandwich('tuna', 'mayonnaise')

