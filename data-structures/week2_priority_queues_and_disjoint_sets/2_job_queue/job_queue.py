# python3

import heapq
from collections import namedtuple


class Worker:
    """Worker class.
    The workers are sorted by release time. If the release time is the same for
    both of them, workers are sorted by their thread_id.
    """

    def __init__(self, thread_id, release_time=0):
        self.thread_id = thread_id
        self.release_time = release_time

    def __lt__(self, other):
        if self.release_time == other.release_time:
            return self.thread_id < other.thread_id
        return self.release_time < other.release_time

    def __gt__(self, other):
        if self.release_time == other.release_time:
            return self.thread_id > other.thread_id
        return self.release_time > other.release_time


AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


class JobQueue:
    def __init__(self, inp1, inp2):
        self.num_workers = inp1
        self.jobs = inp2

    def assign_job(self):
        result = []
        worker_queue = [Worker(i) for i in range(self.num_workers)]

        for job in self.jobs:
            worker = heapq.heappop(worker_queue)

            result.append(AssignedJob(worker.thread_id, worker.release_time))

            worker.release_time += job
            heapq.heappush(worker_queue, worker)
        return result


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job
    return result


def my_assign(n_workers, jobs):
    result = []
    occupied = []
    start = min(n_workers, len(jobs))
    for i in range(start):
        result.append((i, 0))
        occupied.append(jobs[i])
    for i in range(start, len(jobs)):
        get_min = min(occupied)
        get_min_index = occupied.index(get_min)
        result.append((get_min_index, get_min))
        occupied[get_min_index] += jobs[i]
    return result


# my_assign(4, [1 for i in range(20)])


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs
    job_queue = JobQueue(n_workers, jobs)
    assigned_jobs = job_queue.assign_job()

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
