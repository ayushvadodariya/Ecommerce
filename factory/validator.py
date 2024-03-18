class Validator:
    """
    A class for validating the structure and types of elements in a dictionary.

    Attributes:
        None
    """

    def validate_type(self, element, desired_type):
        """
        Validates whether the type of the given element matches the desired type.

        Args:
            element: The element to be validated.
            desired_type: The desired type that the element should match.

        Returns:
            bool: True if the element's type matches the desired type, False otherwise.
        """
        if type(element) == desired_type:
            return True
        else:
            return False

    def validateTypes(self, element, fields):
        """
        Validates the types of elements in the given dictionary against specified types.

        Args:
            element: The dictionary to be validated.
            fields: A dictionary where keys represent fields in the element
                    and values represent the desired types for those fields.

        Returns:
            bool: True if all fields have the correct types, False otherwise.
        """
        for field in fields:
            if field in element:
                if not self.validate_type(element[field], fields[field]):
                    return False
        return True

    def validate(self, element, fields, required_fields, optional_fields):
        """
        Validates the structure and types of the given element against specified fields.

        Args:
            element: The dictionary element to be validated.
            fields: A dictionary where keys represent fields in the element
                    and values represent the desired types for those fields.
            required_fields: A list of required fields that must be present in the element.
            optional_fields: A list of optional fields that may be present in the element.

        Returns:
            bool: True if the element passes all validation checks, False otherwise.

        Raises:
            ValueError: If the element fails any of the validation checks,
                        with an appropriate error message.
        """
        if not self.validateTypes(element, fields):
            return ValueError("Invalid type of field")

        element_fields = set(element.keys())
        required_fields = set(required_fields)
        optional_fields = set(optional_fields)

        if len(required_fields - element_fields) > 0:
            raise ValueError("Missing required fields")

        if len(element_fields - required_fields - optional_fields) > 0:
            raise ValueError("Invalid fields")

        return True