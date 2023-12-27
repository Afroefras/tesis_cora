from typing import Generator, Tuple, List
from pathlib import Path, PosixPath


def get_all_heartpairs(base_dir: str) -> List[Tuple[PosixPath, PosixPath]]:
    ghp = GetHeartPairs(base_dir)
    return [ghp.pair_wav_dat(x) for x in ghp.get_all_wav()]


class GetHeartPairs:
    def __init__(self, base_dir: str) -> None:
        self.base_dir = Path(base_dir)

    def get_all_wav(self) -> Generator[PosixPath, None, None]:
        wav_dirs = self.base_dir.glob("*/*.wav")
        return wav_dirs

    def pair_wav_dat(self, wav_dir: PosixPath) -> Tuple[PosixPath, PosixPath]:
        wav_name = wav_dir.stem
        wav_parent_dir = wav_dir.parent
        dat_dir = wav_parent_dir.joinpath(f"{wav_name}.dat")
        return wav_dir, dat_dir
