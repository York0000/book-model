from django.core.exceptions import ValidationError


def proportion_validator(image):
    if image.height != image.width:
        raise ValidationError('Rasmni bo\'yi va eni bir biriga mos emas')


def page_error(value):
    value = value.strip()
    # value = value.split
    if value.count(' ') != 1:
        raise ValidationError('kamida 2 ta soz bolishi kerak')                                                from django.core.exceptions import ValidationError


def proportion_validator(image):
    if image.height != image.width:
        raise ValidationError('Rasmni bo\'yi va eni bir biriga mos emas')


def page_error(value):
    value = value.strip()
    # value = value.split
    if value.count(' ') != 1:
        raise ValidationError('kamida 2 ta soz bolishi kerak')