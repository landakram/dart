import functools


def inject(model_type,
           to_var=None, from_var=None,
           delete=True, from_val=lambda: None):
    def decorator(view):
        @functools.wraps(view)
        def decorated_view(*args, **kwargs):
            args = list(args)
            key = kwargs.get(from_var) or from_val()
            if not key:
                values = kwargs.values()
                if len(values) > 0:
                    key = values[0]

            model = model_type.query.get(key) if key else None
            if to_var:
                kwargs[to_var] = model
            else:
                args.append(model)
            if from_var in kwargs and delete:
                del kwargs[from_var]

            return view(*args, **kwargs)
        return decorated_view
    return decorator
