dart
======

Dart turns URL variables into database models with a decorator. 

That means you can do something like this:

.. code-block:: python

    @app.route('/user/<user_id>/tracks', methods=['GET'])
    @dart.inject(User, 'user', from_var='user_id')
    def user_tracks(user=None):
        return jsonify(user.tracks)

If you're smart, you might have a decorator that checks user authorization,
something like ``@login_required``. You can compose Dart with other decorators 
to simplify logic, while still keeping your code readable and concise: 

.. code-block:: python

    def login_required(view):
        @functools.wraps(view)
        @dart.inject(User, 'user', from_var='user_id')
        @dart.inject(User, 'current_user', from_val=lambda: session['user_id'])
        def decorated_view(user=None, current_user=None, *args, **kwargs):
            if current_user != user:
                abort(403) 
            else:
                return view(user=user, *args, **kwargs)
        return decorated_view

    @login_required
    def view(user=None):
        return '{} did it!'.format(user.name)

Of course, Dart isn't just a Flask. It's literally just a decorator that
takes a keyword arg or lambda expression and queries the model class using it as 
the primary key. That means you can use the Dart decorator with any function.

For more info, check out the source code -- it's 27 lines.
