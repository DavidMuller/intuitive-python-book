class DinosaurEgg:
    def __init__(self, egg_id):
        self.egg_id = egg_id
        self._hatch_status = None

    def hatch(self):
        if self._hatch_status is not None:
            raise ValueError(
                f"Egg {self.egg_id} has already been hatched."
            )
        self._hatch_status = "hatched"
        print(f"Egg {self.egg_id} has been successfully hatched.")
