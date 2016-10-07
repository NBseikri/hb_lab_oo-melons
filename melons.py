"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """A general melon order."""

    def __init__(self, species, qty, country_code, order_type, tax):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price."""

        base_price = 5

        if self.species.lower() == 'christmas melon':
            base_price = base_price * 1.5  
        
        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            return total + 3

        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        super(DomesticMelonOrder, self).__init__(species, qty, "USA", "domestic", 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        super(InternationalMelonOrder, self).__init__(species, qty, country_code, "international", 0.17)


    # def get_total(self):
    #     normal_total = super(InternationalMelonOrder, self).get_total()
    #     if self.qty < 10:
    #         return normal_total + 3

    #     return normal_total


class GovernmentMelonOrder(AbstractMelonOrder):
    """A US Government melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super(DomesticMelonOrder, self).__init__(species, qty, "USA", "domestic", 0.00)
        self.passed_inspection = False


    def mark_inspection(self, passed):
        """Marked inspection as passed if True."""

        self.passed_inspection = passed 
        # parameter passed is a Boolean, True or False
        # so if mark_inspection(True), can make self.passed_inspection = passed (or True)
        # vice versa for mark_inspection(False)




