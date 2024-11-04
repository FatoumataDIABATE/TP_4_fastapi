from queue import PriorityQueue

from collections import defaultdict


class City:
    def __init__(self, name: str, department: int, country: str, population: int):
        self.name = name
        self.department = department
        self.population = population
        self.country = country

    def __str__(self):
        return f"City: {self.name} has {self.population} inhabitants and is located in {self.department}, {self.country}"

    def __repr__(self):
        return str(self)


class Db:
    def __init__(self, db: list[City]):
        self.cities: dict[str, City] = {city.name: city for city in db}
        self.department_index = dict()
        self.__update_index()
        print("Successfully loaded ", len(db), "cities")

    def add(self, city: City):
        self.cities[city.name] = city
        self.__update_index()

    def delete(self, city_or_dep: str):
        if city_or_dep.isnumeric():  # department
            self.__delete_dep(int(city_or_dep))
            return
        self.__delete_city(city_or_dep)
        self.__update_index()

    def __delete_dep(self, dep):
        for city in self.department_index[dep]:
            self.__delete_city(city.name)
        self.__update_index()

    def __delete_city(self, city):
        del self.cities[city]

    def list_in_department(self, department: int) -> list[City]:
        return self.department_index[department]

    def __getitem__(self, city_name: str):
        if city_name not in self.cities.keys():
            return "<Not Found>"
        return self.cities[city_name]

    def __update_index(self):
        self.department_index = defaultdict(list)
        for city in self.cities.values():
            self.department_index[city.department].append(city)

    def flush(self, path: str):
        with open(path, "wt+") as fp:
            for city in self.cities.values():
                fp.write(f"{city.name},{city.department},{city.country},{city.population}\n")

        print(f"Successfully wrote {len(self.cities)} in {path}")

    def top(self, k: int):
        q = PriorityQueue()
        for city in self.cities.values():
            q.put((city.population, city))
            if len(q.queue) > k:
                q.get()

        res = []
        while len(q.queue):
            res.append(q.get())
        return res
