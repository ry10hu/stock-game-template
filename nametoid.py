def toID(name):
  namestoID = {
      'stock1': 0,
      'stock2': 1,
      'stock3': 2,
      'stock4': 3,
      'stock5': 4,
  }
  # Add more mappings as needed

  # Convert the input string to lowercase for case-insensitive matching
  lower_name = name.lower()

  # Check if the input string is in the mapping, otherwise return a default value (e.g., 0)
  return namestoID.get(lower_name, 0)
