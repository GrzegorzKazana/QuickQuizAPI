from rest_framework.throttling import ScopedRateThrottle
from rest_framework.exceptions import Throttled


class QuizPostThrottle(ScopedRateThrottle):
    scope_attr = 'quiz_post_throttle_scope'
