# first line: 330
        @functools.wraps(
            f, functools.WRAPPER_ASSIGNMENTS + ("__defaults__", "__kwdefaults__")
        )
        def wrapped_f(*args: t.Any, **kw: t.Any) -> t.Any:
            # Always create a copy to prevent overwriting the local contexts when
            # calling the same wrapped functions multiple times in the same stack
            copy = self.copy()
            wrapped_f.statistics = copy.statistics  # type: ignore[attr-defined]
            return copy(f, *args, **kw)
