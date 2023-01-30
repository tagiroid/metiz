def get_formatted_cities(country, city, population=''):
    if population:
        formatted = f'{city}, {country} - population {population}'
    else:
        formatted = f'{city}, {country}'
    return formatted.title()
