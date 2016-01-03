from locust import HttpLocust, TaskSet, task


class HitMeTasks(TaskSet):
    @task(3)
    def index(self):
        self.client.get("/")

    @task(10)
    def test200ms(self):
        self.client.get("/200ms")

    @task(1)
    def test2s(self):
        self.client.get("/2000ms")

    @task(1)
    def test10s(self):
        self.client.get("/10000ms")

    @task(1)
    def increment(self):
        self.client.get("/increment")


class HitMeLocust(HttpLocust):
    host = "http://hit--me.herokuapp.com"
    task_set = HitMeTasks
    min_wait = 5000
    max_wait = 15000
