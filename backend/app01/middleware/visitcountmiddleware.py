import time

from django.core.cache import cache


class VisitCountMiddleware(object):
    """ 流量统计 """

    def __init__(self, get_response):
        self.get_response = get_response
        self.count = {}

    def __call__(self, request):
        if request.META.has_key("HTTP_X_FORWARDED_FOR"):
            ip = request.META["HTTP_X_FORWARDED_FOR"]
        else:
            ip = request.META["REMOTE_ADDR"]

        response = self.get_response(request)

        stats = cache.get_or_set("stats", {})
        count = 0
        count += 1  # 次数没统计 只统计了一次 怎么解决？
        if not stats.get(ip):
            stats[ip] = [time.time(), count]  # 设置时间戳，计算某段时间的流量
            cache.set("stats", stats, 60)

        return response
