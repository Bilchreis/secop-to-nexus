from secop_to_nexus.nxs_base_classes.NXobject import NXobject


class NXreference:
    target: NXobject = None
    path: str = ""

    def _init__(self, target: NXobject):
        self.target = target
        self.path = target.get_path()

    def __call__(self) -> str:
        return self.path
