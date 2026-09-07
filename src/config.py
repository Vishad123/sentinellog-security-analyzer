from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    failure_threshold: int = 5
    multi_user_threshold: int = 3
    success_after_failure_window_minutes: int = 15
    failure_window_minutes: int = 15
    normal_start_hour: int = 7
    normal_end_hour: int = 22
    failure_score: int = 1
    multi_user_score: int = 5
    success_after_failure_score: int = 5
    unusual_hour_score: int = 3
