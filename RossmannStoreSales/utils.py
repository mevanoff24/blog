import pandas as pd
import numpy as np
import re
from pandas.api.types import is_string_dtype, is_numeric_dtype
from sklearn.preprocessing import StandardScaler
import warnings
from sklearn.exceptions import DataConversionWarning
from sklearn_pandas import DataFrameMapper
warnings.filterwarnings('ignore', category=DataConversionWarning)


def transform_date(df, field_name, drop=True):
    field = df[field_name]
    if not np.issubdtype(field, np.datetime64):
        df[field_name] = field = pd.to_datetime(field, infer_datetime_format=True)
    target_pre = re.sub('[Dd]ate$', '', field_name)
    for i in ('Year', 'Month', 'Week', 'Day', 'Dayofweek', 'Dayofyear', 'Weekofyear',
            'Is_month_end', 'Is_month_start', 'Is_quarter_end', 'Is_quarter_start', 'Is_year_end', 'Is_year_start'):
        df[target_pre + i] = getattr(field.dt, i.lower())
    df[target_pre + 'Elapsed'] = field.astype(np.int64) // 10**9
    if drop:
        df.drop(field_name, axis=1, inplace=True)