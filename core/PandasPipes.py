import pandas as pd

class PandasPipes:
    def join(leftdf, rightdf, left_index, right_index, validate, how):
        return pd.merge(leftdf.set_index(left_index), rightdf.set_index(right_index), left_on=left_index, right_on=right_index, left_index=True, right_index=True, how=how, validate=validate)
       
