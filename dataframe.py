# What is the goal?
# take data, organize it into a 2D data structure
# data can be added manually
# data can be added from a dictionary
# data can be added from a CSV
# data can be written to a CSV file

class DataFrame:
    _data = {}  # columns will be key value pairs, where the key is the column name, and the column is a list
                # the columns (lists) in the dict must all be the same length
    _length = 0

    def __init__(self, data=None):
        if data != None:
            self._data = self._validate_data(data) # this doesn't work, as there would need to be checking
        print("Dataframe created")

    # END __init__()

    def _validate_data(self, data):
        if not isinstance(data, dict):
            raise ValueError(f"DataFrame data must be 'dict' but was actually {type(data)}")

        # check each column
        # check the column is type list
        # check that all column lengths are the same
        col_lengths = []
        for key in data:
            if not isinstance(data[key], list):
                raise ValueError(f"DataFrame values must be 'list' but was actually {type(data[key])}")

            col_lengths.append(len(data[key]))

        for i in range(0, len(col_lengths) - 1):
            if col_lengths[i] != col_lengths[i + 1]:
                raise IndexError(f"Column lengths must all be the same size. Sizes: {col_lengths}")
        
        if len(col_lengths) > 0:
            self._length = col_lengths[0]

        data['index'] = [int(i) for i in range(0, len(data))]

        return data
    # END _validate_columns()

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, _data):
        self._data = self._validate_data(_data)

    def column_names(self):
        return list(self._data.keys())
    
    def __str__(self):
        data_str = ""
        for key in self._data:
            data_str = data_str + str(key) + '\t'
        data_str = data_str + '\n'
        
        for i in range(0, self._length):
            for key in self._data:
                data_str = data_str + str(self._data[key][i]) + '\t'
            data_str = data_str + '\n' 

        return data_str

    def __len__(self):
        return self._length

    def add_row(self, row):
        if len(row) != len(self._data):
            print(f"Row must have correct number of elements. Provided: {len(row)}, Needed: {len(self._data)}")
            print("Dropping provided row.")
            return # no need to continue, as the rows don't match. But the program doesn't need to break either.
        row_index = 0
        for key in self._data:
            self._data[key].append(row[row_index])
            row_index += 1
        self._length += 1

    def __getitem__(self, key):
        if key in self._data:
            return self._data[key]
        else:
            raise KeyError(f"[{key}] not found in DataFrame")
        
    def __setitem__(self, key, value):
        if not isinstance(value, list):
            raise ValueError(f"New column data must be a list but got {type(value)} instead")
        
        if len(value) != self._length:
            raise ValueError(f"New column length does not match current DataFrame length")
        
        self._data[key] = value
        if not self._data:
            self._length = len(value)
        


mydict = {'key1': [0, 1, 5], 'key2': [0, 2, 1], 'key3': [10, 1, 5]}

df = DataFrame(mydict)



df['new_key'] = [1, 2, 3]
print(df)