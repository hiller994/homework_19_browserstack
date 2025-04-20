def abs_path_from_project(relative_path: str):
    import hw_19_browserstack
    from pathlib import Path

    return (
        Path(hw_19_browserstack.__file__).parent.parent.joinpath(relative_path).absolute().__str__()
    )