#If you want, go ahead and just go for it with these free public data set resources:
#
# http://www.data.gov/
#
# http://aws.amazon.com/public-data-sets/
#
# http://www.google.com/publicdata/directory
#
# Import train.csv from:
# https://www.kaggle.com/c/titanic-gettingStarted
#Now let's open it with pandas
import pandas as pd
from pandas import Series,DataFrame
# Set up the Titanic csv file as a DataFrame
titanic_df = pd.read_csv('train.csv')
# Let's see a preview of the data
titanic_df.head()
# We could also get overall info for the dataset
titanic_df.info()
# Now let's get a simple visualization!
#sns.factorplot('Alone',data=titanic_df,palette='Blues')

