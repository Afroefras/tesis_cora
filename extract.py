from typing import Generator, Tuple, List
from pathlib import Path, PosixPath


def get_all_heartpairs(base_dir: str) -> List[Tuple[PosixPath, PosixPath]]:
    ghp = GetHeartPairs(base_dir)
    return [ghp.pair_dat_wav(x) for x in ghp.get_all_dat()]


class GetHeartPairs:
    def __init__(self, base_dir: str) -> None:
        self.base_dir = Path(base_dir)

    def get_all_dat(self) -> Generator[PosixPath, None, None]:
        dat_dirs = self.base_dir.glob("*/*.dat")
        return dat_dirs

    def pair_dat_wav(self, dat_dir: PosixPath) -> Tuple[PosixPath, PosixPath]:
        dat_name = dat_dir.stem
        dat_parent_dir = dat_dir.parent
        wav_dir = dat_parent_dir.joinpath(f"{dat_name}.wav")
        return dat_dir, wav_dir
