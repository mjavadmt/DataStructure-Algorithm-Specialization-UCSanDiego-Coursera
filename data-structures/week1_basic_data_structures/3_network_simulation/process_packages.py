# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


def has_condition_to_remove(request, finishes_time):
    for p in finishes_time:
        if request[0] >= p:
            return True, p
    return False, 0


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        while self.finish_time and self.finish_time[0] <= request[0]:
            self.finish_time.remove(self.finish_time[0])
        if len(self.finish_time) == 0:
            self.finish_time.append(request[1] + request[0])
            return Response(False, request[0])
        elif len(self.finish_time) < self.size:
            self.finish_time.append(request[1] + self.finish_time[-1])
            return Response(False, self.finish_time[-2])
        elif len(self.finish_time) == self.size:
            return Response(True, -1)
        return Response(False, -1)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


b1 = Buffer(1)
responses = process_requests([[0, 0],[0,0]], b1)
for response in responses:
    print(response.started_at if not response.was_dropped else -1)

def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
