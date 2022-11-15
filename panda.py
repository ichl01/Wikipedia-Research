import numpy as np
c_list = [0,1,2,1]
num = np.percentile(c_list, q=[50])
if num == 1:
    print(num)
#c_df.quantile(q=[0, 0.25, 0.5, 0.75, 1])