"""
This program reads contact information from a CSV file and stores it in a nested dictionary.

"""

def read_file(filename):
    """
    Reads contact information from a CSV file and returns it as a nested dictionary.

    Args:
        filename: The name of the CSV file to read.

    Returns:
        dict: A dictionary where each key is the contact's key and the value is another
              dictionary containing the contact's information .
    """
    data = {}
    with open(filename, mode='r', encoding='utf-8') as file:

        lines = file.readlines()
        headers = lines[0].strip().split(';')
        
        for line in lines[1:]:
            fields = line.strip().split(';')
            key = fields[0]
            contact_info = {headers[i]: fields[i] for i in range(1, len(headers))}
            data[key] = contact_info
    
    return data


