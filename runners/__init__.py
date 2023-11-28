REGISTRY = {}

from .episode_runner import EpisodeRunner
REGISTRY["episode"] = EpisodeRunner

from .parallel_runner import ParallelRunner
REGISTRY["parallel"] = ParallelRunner

from .smmae_episode_runner import SMMAEEpisodeRunner
REGISTRY["smmae_episode"] = SMMAEEpisodeRunner
