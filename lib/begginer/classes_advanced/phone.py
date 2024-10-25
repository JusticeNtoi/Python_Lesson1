from item import Item


class Phone(Item):

    def __init__(self, broken_phones: int = 0, **kwargs):
        # Call to super function to have access to all attributes / methods
        super().__init__(**kwargs)
        # Run validations on received arguments
        assert (
            broken_phones >= 0
        ), f"Broken Phones {broken_phones} is not greater or equal to zero!"

        # Assign to self object
        self.broken_phones = broken_phones
