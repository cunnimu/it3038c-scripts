
Pandas is used to manipulate and analyze data sets.

To create a virtual env with pandas:
```
virtualenv ~/venv/pandas
source ~/venv/pandas/bin/activate
pip install pandas
```

Pandas is imported with the alias `pd`
```
import pandas as pd
```

A dataframe is a datastructure that can be used in pandas. It's similar to a table, like in a spreadsheet or sql. To manually create a simple dataframe (of household pets) in pandas:
```
import pandas as pd

df = pd.DataFrame(
	{
		"Name": [
			"Lucy",
			"Thor",
			"Jenga"
		],
		"Age": [7, 11, 4],
		"Species": ["dog", "dog", "cat"]
	}
)
print(df)
```

To save this dataframe to a csv use the `to_csv()` method:
```
df.to_csv('data.csv')
```

Pandas can be used with many forms of data. To create a dataframe from a csv use `read_csv()` method:
```
import pandas as pd

df = pd.read_csv('data.csv')
```

To get information about the dataframe, use the `info()` method. This returns the data type of each column and memory usage.
```
print(df.info())
```

This is a very, very brief look at what pandas is capable of. When finished, quit python and deactivate the virtual env:
```
quit()
deactivate
```