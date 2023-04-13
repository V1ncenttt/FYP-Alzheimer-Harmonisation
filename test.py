from neuroharmony import exclude_single_subject_groups, fetch_sample, Neuroharmony
from neuroharmony.data.rois import rois
# Load the data.
# You can do as you wish, as long as the input to Neuroharmony is a NDFrame (pandas).
X = fetch_sample()
features = rois
covariates = ["Gender", "scanner", "Age"]
exclude_vars = X.columns[X.isna().sum() != 0].to_list() + X.columns[X.dtypes == 'O'].to_list() + ['Dataset', 'Diagn']
regression_features = [var for var in X.columns if var not in covariates + features + exclude_vars]

eliminate_variance = ["scanner"]

X.Age = X.Age.astype(int)
scanners = X.scanner.unique()
n_scanners = len(scanners)
# Split train and test leaving one scanner out.
train_bool = X.scanner.isin(scanners[1:])
test_bool = X.scanner.isin(scanners[:1])
X_train_split = X[train_bool][regression_features + covariates + rois]
X_test_split = X[test_bool][regression_features + covariates + rois]
x_train, x_test = X_train_split, X_test_split
x_train = exclude_single_subject_groups(x_train, covariates)

# Create the Neuroharmony model.
# Here you can establish the range of the hyperparameters via random search or give specific values.
harmony = Neuroharmony(
    features,
    regression_features,
    covariates,
    eliminate_variance,
    param_distributions=dict(
        RandomForestRegressor__n_estimators=[100, 200, 500],
        RandomForestRegressor__random_state=[42, 78],
        RandomForestRegressor__warm_start=[False, True],
    ),
    estimator_args=dict(n_jobs=1, random_state=42),
    randomized_search_args=dict(cv=5, n_jobs=8),
)
# Fit the model.
x_train_harmonized = harmony.fit_transform(x_train)