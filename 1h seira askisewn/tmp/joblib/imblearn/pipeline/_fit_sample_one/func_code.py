# first line: 602
def _fit_sample_one(sampler, X, y, **fit_params):
    X_res, y_res = sampler.fit_sample(X, y, **fit_params)

    return X_res, y_res, sampler
