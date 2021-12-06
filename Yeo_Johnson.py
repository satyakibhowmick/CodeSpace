from scipy import stats

def skew_handling(df):
	'''Separates the numeric and categorical columns,
	then separates the discrete and continuous columns
	from the numeric columns'''

	num_cols = []
	cat_cols = []

	for i in df.columns:
		if df[i].dtype in ['int64', 'float64']:
			num_cols.append(i)
		else:
			cat_cols.append(i)

	disc_num_cols = []
	cont_num_cols = []

	for j in num_cols:
		if df[j].nunique() <= 20:
			disc_num_cols.append(j)
		else:
			cont_num_cols.append(j)

	'''Transforms the continuous numeric columns
	and adds new transformed columns at the end
	of the dataframe'''

	k = [l + '_transformed' for l in cont_num_cols]

	for m, n in zip(cont_num_cols, k):
		o, p = stats.yeojohnson(df[m])
		df[n] = o

	return df
